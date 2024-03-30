# TODO: Checkout GDT format: num_models is fixed to 13 for some reason?
import os
import bpy

from .kaitai.prism3d_gdt import Prism3dGdt
from .kaitai.prism3d_pmd import Prism3dPmd
from .kaitai.prism3d_pmg import Prism3dPmg
from .kaitai.prism3d_psm import Prism3dPsm

# V003: Shark: Hunting the great white
# V005: 911FireRescue,
# V006: DukeNukem: Manhattan Project, 18woS: Hard Truck, Hunting Unlimited 1, Hunting Unlimited 2,
# V007: OceanDive 1.4, Hunting Unlimited 3
#
# https://www.moddb.com/games/duke-nukem-manhattan-project/downloads <= Tools for V006
def import_gdt(context, filepath, mat):
    name, _ = os.path.splitext(os.path.basename(filepath))
    #filedir = os.path.dirname(filepath)

    parsed = Prism3dGdt.from_file(filepath)
    print(parsed)

    view_layer = bpy.context.view_layer
    collection = view_layer.active_layer_collection.collection

    #root = bpy.data.objects.new(name)
    #collection.objects.link(root)

    for m in parsed.models:
        mverts = list(map(lambda v: [v.x, v.y, v.z], m.vertices))
        mfaces = []
        muvs = []
        for i in range(0, len(m.indices), 3):
            a = m.indices[i]
            b = m.indices[i+1]
            c = m.indices[i+2]
            mfaces.append([ a,b,c ])
            muvs.append([ m.uvs[a].u, m.uvs[a].v ])
            muvs.append([ m.uvs[b].u, m.uvs[b].v ])
            muvs.append([ m.uvs[c].u, m.uvs[c].v ])

        mesh_data = bpy.data.meshes.new(name + '_Mesh')
        mesh_data.from_pydata(mverts, [], mfaces) # [] = no edges defined
        mesh_data.update()

        obj = bpy.data.objects.new(name, mesh_data)
        collection.objects.link(obj)

        # Configure uv layer
        uv = obj.data.uv_layers.new(name=name + "_UV")
        for loop in obj.data.loops:
            uv.data[loop.index].uv = muvs[loop.index]

    return {'FINISHED'}

#  4: 18WoS: Convoy, Bus Driver, Deer Drive, Hunting Unlimited 4, Hunting Unlimited 2008, Hunting Unlimited 2009, Hunting Unlimited 2010, 
#  5: 911 Fire Rescue
#  7,8: Shark: Hunting the great white, 
#  9: Hunting Unlimited 1, 
# 10: 18WoS: Across America, 18WoS: Hard Truck
def import_pmd(context, filepath, mat):
    name, _ = os.path.splitext(os.path.basename(filepath))
    #filedir = os.path.dirname(filepath)

    parsed = Prism3dPmd.from_file(filepath)

    view_layer = bpy.context.view_layer
    collection = view_layer.active_layer_collection.collection

    for idx in range(parsed.num_objects):
        h = parsed.object_headers[idx]
        o = parsed.objects[idx]

        mverts = list(map(lambda v: [v.x, v.y, v.z], o.vertices))
        mfaces = []
        muvs = []
        for i in range(0, o.num_indices, 3):
            a = o.indices[i]
            b = o.indices[i+1]
            c = o.indices[i+2]
            mfaces.append([ a,b,c ])
            muvs.append([ o.uvs[a].x, o.uvs[a].y ])
            muvs.append([ o.uvs[b].x, o.uvs[b].y ])
            muvs.append([ o.uvs[c].x, o.uvs[c].y ])

        mesh_data = bpy.data.meshes.new(h.name + '_Mesh')
        mesh_data.from_pydata(mverts, [], mfaces) # [] = no edges defined
        mesh_data.update()

        obj = bpy.data.objects.new(h.name, mesh_data)
        collection.objects.link(obj)

    # TODO: uv + animation

    return {'FINISHED'}

# 0x10: 18WoS: Convoy, Hunter Unlimited 4
# 0x11: Bus Driver, Deer Drive, Hunting Unlimited 2008, Hunting Unlimited 2009, Hunting Unlimited 2010,
def import_pmg(context, filepath, mat):
    name, _ = os.path.splitext(os.path.basename(filepath))
    #filedir = os.path.dirname(filepath)

    parsed = Prism3dPmg.from_file(filepath)

    view_layer = bpy.context.view_layer
    collection = view_layer.active_layer_collection.collection

    for o in parsed.objects:
        mverts = list(map(lambda v: [v.x, v.y, v.z], o.vertices))
        mfaces = []
        muvs = []
        for i in range(0, len(o.indices), 3):
            a = o.indices[i]
            b = o.indices[i+1]
            c = o.indices[i+2]
            mfaces.append([ a,b,c ])
            muvs.append([ o.uvs[a].x, o.uvs[a].y ])
            muvs.append([ o.uvs[b].x, o.uvs[b].y ])
            muvs.append([ o.uvs[c].x, o.uvs[c].y ])

        mesh_data = bpy.data.meshes.new(name + '_Mesh')
        mesh_data.from_pydata(mverts, [], mfaces) # [] = no edges defined
        mesh_data.update()

        obj = bpy.data.objects.new(name, mesh_data)
        collection.objects.link(obj)

    return {'FINISHED'}

#  3: Hunting Unlimited 1, 
#  4: 10WoS: Hard Truck, 
#  6: 18WoS: Across America, Hunting Unlimited 2, Hunting Unlimited 3,
#  7: 18WoS: Pedal to the Metal, Hunting Unlimited 3, 
#  9: OceanDive 1.4, 
def import_psm(context, filepath, mat):
    name, _ = os.path.splitext(os.path.basename(filepath))
    #filedir = os.path.dirname(filepath)

    parsed = Prism3dPsm.from_file(filepath)

    view_layer = bpy.context.view_layer
    collection = view_layer.active_layer_collection.collection

    for o in parsed.objects:
        mverts = list(map(lambda v: [v.x, v.y, v.z], o.vertices))
        mfaces = []
        muvs = []
        for i in range(0, o.num_triangles * 3, 3):
            a = o.indices[i]
            b = o.indices[i+1]
            c = o.indices[i+2]
            mfaces.append([ a,b,c ])
            muvs.append([ o.uvs[a].x, o.uvs[a].y ])
            muvs.append([ o.uvs[b].x, o.uvs[b].y ])
            muvs.append([ o.uvs[c].x, o.uvs[c].y ])

        mesh_data = bpy.data.meshes.new(o.name + '_Mesh')
        mesh_data.from_pydata(mverts, [], mfaces) # [] = no edges defined
        mesh_data.update()

        obj = bpy.data.objects.new(o.name, mesh_data)
        collection.objects.link(obj)

    return {'FINISHED'}
