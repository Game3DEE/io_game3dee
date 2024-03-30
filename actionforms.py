import os
import bpy
from .textures import create_material
from .kaitai.animator_3df import Animator3df
from .kaitai.carnivores_3df import Carnivores3df

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

    height = (parsed.len_texture / 2) / 256

    mverts = list(map(lambda v: [v.x, v.y, v.z], parsed.vertices))
    mfaces = []
    muvs = []
    for f in parsed.faces:
        muvs.append([ f.u[0] / 255.0, (255.0 - f.tay) / height ])
        muvs.append([ f.u[1] / 255.0, (255.0 - f.tby) / height ])
        muvs.append([ f.u[2] / 255.0, (255.0 - f.tcy) / height ])
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
