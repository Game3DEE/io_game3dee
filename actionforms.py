import os
import bpy
from .textures import create_material, create_material_from_image
from .kaitai.animator_3df import Animator3df
from .kaitai.carnivores_3df import Carnivores3df
from .kaitai.atmosfear_ubfc import AtmosfearUbfc

"""
Carnivores face flags:
#define sfDoubleSide         1
#define sfDarkBack           2
#define sfOpacity            4
#define sfTransparent        8
#define sfMortal        0x0010
#define sfPhong         0x0030
#define sfEnvMap        0x0050

#define sfNeedVC        0x0080
#define sfDark          0x8000

"""

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
                tri_count = 0
                quad_count = 0
                for face in block.data.faces:
                    faces.append([ face.c, face.b, face.a ])
                    if face.d != face.c: # is this face a quad?
                        faces.append([ face.a, face.d, face.c ])
                        quad_count += 1
                    else:
                        tri_count += 1
                print("Tris:%d, Quads:%d" % (tri_count, quad_count))

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

    create_alpha = False
    for f in parsed.faces:
        if f.flags & 4 == 4:
            create_alpha = True

    height, image = image_from_data(parsed.len_texture, parsed.texture, create_alpha)

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
    mat = create_material_from_image(name, image)
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

def image_from_data(texture_size, data, create_alpha = False):
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
            a = 1.0
            if create_alpha:
                a = 0.0 if w == 0 else 1.0
            p[dest + 0] = r / 31.0
            p[dest + 1] = g / 31.0
            p[dest + 2] = b / 31.0
            p[dest + 3] = a
            dest += 4
        image.pixels[:] = p[:]
        image.pack()
        image.use_fake_user = True

    return height, image
