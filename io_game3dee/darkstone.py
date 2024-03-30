import os
import re
import bpy

from .kaitai.darkstone_o3d import DarkstoneO3d
from .textures import create_material

def find_texture_dir(base_dir):
    for i in range(6): # random number; low enough not to cause performance issues
        test_dir = os.path.join(base_dir, 'bankdatabase')
        if os.path.isdir(test_dir):
            dbd = os.path.join(test_dir, 'dragonblade')
            if os.path.isdir(dbd):
                return dbd

        bn = os.path.basename(base_dir)
        base_dir = base_dir[:len(base_dir)-(len(bn)+1)]

    return None

def import_o3d(context, filepath, mat):
    name, ext = os.path.splitext(os.path.basename(filepath))
    filedir = os.path.dirname(filepath)

    o3d = DarkstoneO3d.from_file(filepath)

    # create list of vertices
    mverts = list(map(lambda v: [v.x, v.y, v.z], o3d.vertices))

    # create lists for faces & attributes
    mfaces = []
    muvs = []
    for f in o3d.faces:
        count = 3 if f.indices[3] == 0xffff else 4
        mfaces.append(f.indices[:count])
        muvs += list(map(lambda uv: [ uv.x / 255.0, 1 - (uv.y / 255.0) ], f.tex_coords[:count]))

    mesh_data = bpy.data.meshes.new(name + '_Mesh')
    mesh_data.from_pydata(mverts, [], mfaces) # [] = no edges defined
    mesh_data.update()
    mesh_data.transform(mat)

    obj = bpy.data.objects.new(name, mesh_data)

    # print unique texture IDs
    unique_materials = list(dict.fromkeys(list(map(lambda f: f.tex_number, o3d.faces))))

    tdir = find_texture_dir(filedir)
    all_textures = os.listdir(tdir)
    for texnum in unique_materials:
        result = list(filter(lambda fname: re.match("^[a-z]%04d.*.tga$" % texnum, fname), all_textures))
        obj.data.materials.append(create_material("dragonblade_%04d" % texnum,
            os.path.join(tdir, result[0]) if len(result) > 0 else None))

    for i in range(len(o3d.faces)):
        obj.data.polygons[i].material_index = unique_materials.index(o3d.faces[i].tex_number)

    # Set UV mapping
    uv = obj.data.uv_layers.new(name=name + "_UV")
    for loop in obj.data.loops:
        uv.data[loop.index].uv = muvs[loop.index]

    view_layer = bpy.context.view_layer
    collection = view_layer.active_layer_collection.collection
    collection.objects.link(obj)
