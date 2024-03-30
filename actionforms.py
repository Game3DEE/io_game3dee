import os
import bpy
from .kaitai.animator_3df import Animator3df
from .textures import create_material

def import_animator_3df(context, filepath, mat):
    name, ext = os.path.splitext(os.path.basename(filepath))
    filedir = os.path.dirname(filepath)

    parsed = None
    try:
        parsed = Animator3df.from_file(filepath)
    except:
        pass

    if parsed is None:
        return {'CANCELLED'}

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
