import os
import bpy
from .textures import create_material
from .kaitai.animator_3df import Animator3df
from .kaitai.carnivores_3df import Carnivores3df
from .kaitai.atmosfear_ubfc import AtmosfearUbfc

def import_ubfc(context, filepath, mat):
    parsed = AtmosfearUbfc.from_file(filepath)

    view_layer = bpy.context.view_layer
    collection = view_layer.active_layer_collection.collection

    verts = []
    faces = []
    obj_count = 0
    for block in parsed.blocks:
        match block.id:
            case AtmosfearUbfc.BlockId.object_start:
                if len(verts) > 0:
                    obj_count += 1
                    name = "Object%d" % obj_count
                    mesh_data = bpy.data.meshes.new(name + '_Mesh')
                    mesh_data.from_pydata(verts, [], faces) # [] = no edges defined
                    mesh_data.update()
                    mesh_data.transform(mat)

                    obj = bpy.data.objects.new(name, mesh_data)
                    collection.objects.link(obj)

                    verts = []
                    faces = []
            case AtmosfearUbfc.BlockId.vertices:
                verts = list(map(lambda v: [v.x, v.y, v.z], block.data.vertices))
            case AtmosfearUbfc.BlockId.faces:
                for face in block.data.faces:
                    if face.d != face.c: # is this face a quad?
                        faces.append([ face.a, face.b, face.c, face.d ])
                    else:
                        faces.append([ face.a, face.b, face.c ])

    if len(verts) > 0:
        obj_count += 1
        name = "Object%d" % obj_count
        mesh_data = bpy.data.meshes.new(name + '_Mesh')
        mesh_data.from_pydata(verts, [], faces) # [] = no edges defined
        mesh_data.update()
        mesh_data.transform(mat)

        obj = bpy.data.objects.new(name, mesh_data)
        collection.objects.link(obj)

    return {'FINISHED'}

def import_3df(context, filepath, mat):
    try:
        return import_animator_3df(context, filepath, mat)
    except:
        pass

    return import_carnivores_3df(context, filepath, mat)

def import_carnivores_3df(context, filepath, mat):
    name, _ = os.path.splitext(os.path.basename(filepath))

    parsed = Carnivores3df.from_file(filepath)

    view_layer = bpy.context.view_layer
    collection = view_layer.active_layer_collection.collection

    height, image = read_texture(parsed.len_texture, parsed.texture)

    mverts = list(map(lambda v: [v.x, v.y, v.z], parsed.vertices))
    mfaces = []
    muvs = []
    for f in parsed.faces:
        muvs.append([ f.u[0] / 255.0, (255.0 - f.v[0]) / height ])
        muvs.append([ f.u[1] / 255.0, (255.0 - f.v[1]) / height ])
        muvs.append([ f.u[2] / 255.0, (255.0 - f.v[2]) / height ])
        mfaces.append(f.indices)

    mesh_data = bpy.data.meshes.new(name + '_Mesh')
    mesh_data.from_pydata(mverts, [], mfaces) # [] = no edges defined
    mesh_data.update()
    mesh_data.transform(mat)

    obj = bpy.data.objects.new(name, mesh_data)
    collection.objects.link(obj)

    uv = obj.data.uv_layers.new(name=name + "_UV")
    for loop in obj.data.loops:
        uv.data[loop.index].uv = muvs[loop.index]

    # If we have a texture, setup material
    if image != None:
        mat = bpy.data.materials.new(name=name + "_Material")
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes["Principled BSDF"]
        texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
        texImage.image = image
        mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])
        obj.data.materials.append(mat)

    return {'FINISHED'}

def import_animator_3df(context, filepath, mat):
    name, _ = os.path.splitext(os.path.basename(filepath))
    filedir = os.path.dirname(filepath)

    parsed = Animator3df.from_file(filepath)

    # Create required materials
    materials = list(map(lambda tex: create_material(name + "_" + os.path.basename(tex),
        os.path.join(filedir, tex)), parsed.textures))

    view_layer = bpy.context.view_layer
    collection = view_layer.active_layer_collection.collection

    lod_num = 0
    for lod in parsed.lods:
        mverts = list(map(lambda v: [v.x, v.y, v.z], lod.vertices))
        mfaces = []
        muvs = []
        for f in lod.faces:
            muvs.append([ f.tax, 1. - f.tay ])
            muvs.append([ f.tbx, 1. - f.tby ])
            muvs.append([ f.tcx, 1. - f.tcy ])

            mfaces.append([ f.a, f.b, f.c ])

        mesh_data = bpy.data.meshes.new(name + '_Mesh')
        mesh_data.from_pydata(mverts, [], mfaces) # [] = no edges defined
        mesh_data.update()
        mesh_data.transform(mat)

        obj = bpy.data.objects.new(name + "_LOD%d" % lod_num, mesh_data)
        collection.objects.link(obj)

        if lod_num >= 1:
            obj.hide_set(True)

        for m in materials:
            obj.data.materials.append(m)

        # Set materials (per face)
        face_index = 0
        for materialIdx in range(parsed.num_textures):
            for i in range(lod.face_by_texture_counts[materialIdx]):
                obj.data.polygons[face_index].material_index = materialIdx
                face_index += 1

        uv = obj.data.uv_layers.new(name=name + "_UV")
        for loop in obj.data.loops:
            uv.data[loop.index].uv = muvs[loop.index]

        lod_num += 1

    return {'FINISHED'}

def read_texture(texture_size, data):
    height = int((texture_size / 2) / 256)
    if height == 0:
        height = 256

    image = None
    offset = 0
    if len(data) > 0:
        image = bpy.data.images.new('src', 256, height)
        p = [0.0] * 256 * height * 4
        # convert BGR5551 to RGBA
        dest = 0
        for pixels in range(int(texture_size / 2)):
            w = data[offset+0] + (data[offset+1] * 256)
            offset += 2
            b = (w >> 0) & 31
            g = (w >> 5) & 31
            r = (w >> 10) & 31
            p[dest + 0] = r / 31.0
            p[dest + 1] = g / 31.0
            p[dest + 2] = b / 31.0
            p[dest + 3] = 1.0
            dest += 4
        image.pixels[:] = p[:]
        image.pack()
        image.use_fake_user = True

    return height, image
