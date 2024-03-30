import os
import bpy

from .kaitai.canopygames_mdl import CanopygamesMdl
from .textures import create_material

def import_mdl(context, filepath, mat):
    name, _ = os.path.splitext(os.path.basename(filepath))
    filedir = os.path.dirname(filepath)

    parsed = CanopygamesMdl.from_file(filepath)

    poly_textures = ()
    vertices = ()
    index = ()
    uvs = ()

    materials = []

    for el in parsed.elements:
        if el.type == "SRMESHMODEL":
            for attr in el.attributes:
                print(attr.key)
                if attr.key == "VERTEXLOC":
                    print(attr.value.num_vertices)
                    vertices = attr.value.vertices
                elif attr.key == "POLYVERTEX":
                    print(attr.value.num_polies)
                    index = attr.value.indices
                    print(len(index))
                elif attr.key == "TEXCOORDS_PASS_0":
                    print(attr.value.num_uvs)
                    uvs = attr.value.uvs
                elif attr.key == "POLYTEXTURE_PASS_0":
                    print(attr.value.num_poly_textures)
                    poly_textures = attr.value.poly_textures
        elif el.type == "TEXTURE":
            for attr in el.attributes:
                if attr.key == "TEXTUREFILE":
                    texpath = os.path.join(filedir, "..", "images", attr.value.string)
                    print(texpath)
                    materials.append(create_material(attr.value.string, texpath))

    if len(vertices) > 0 and len(index) > 0 and len(uvs) > 0 and len(poly_textures) > 0:
        view_layer = bpy.context.view_layer
        collection = view_layer.active_layer_collection.collection
        
        mverts = list(map(lambda v: [v.x, v.y, v.z], vertices))
        mfaces = []
        muvs = []
        for i in range(0, len(index), 3):
            a = index[i]
            b = index[i+1]
            c = index[i+2]
            mfaces.append([ a,b,c ])
            muvs.append([ uvs[a].x, uvs[a].y ])
            muvs.append([ uvs[b].x, uvs[b].y ])
            muvs.append([ uvs[c].x, uvs[c].y ])

        mesh_data = bpy.data.meshes.new(name + '_Mesh')
        mesh_data.from_pydata(mverts, [], mfaces) # [] = no edges defined
        mesh_data.update()

        obj = bpy.data.objects.new(name, mesh_data)
        collection.objects.link(obj)

        # Add materials to object
        for material in materials:
            obj.data.materials.append(material)

        # Assign materials to polygons
        for poly_index in range(len(mfaces)):
            obj.data.polygons[poly_index].material_index = poly_textures[poly_index]

        # Configure uv layer
        uv = obj.data.uv_layers.new(name=name + "_UV")
        for loop in obj.data.loops:
            uv.data[loop.index].uv = muvs[loop.index]
    else:
        print("No mesh was found!")

    return {'FINISHED'}
