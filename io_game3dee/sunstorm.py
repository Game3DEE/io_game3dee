import os
import bpy

from .kaitai.sunstorm_ssm import SunstormSsm
from .kaitai.sunstorm_stx import SunstormStx
from .textures import create_material

# TODO: fix assumption of 24bit textures
def import_stx(name, path):
    stx = SunstormStx.from_file(path)
    mipmap = stx.mipmaps[0]
    pixel_count = mipmap.width * mipmap.height
    img = bpy.data.images.new(name, mipmap.width, mipmap.height)
    p = [0.0] * pixel_count * 4
    for i in range(pixel_count):
        p[i * 4 +0] = mipmap.rgb[i * 3 +0] / 255.0
        p[i * 4 +1] = mipmap.rgb[i * 3 +1] / 255.0
        p[i * 4 +2] = mipmap.rgb[i * 3 +2] / 255.0
        p[i * 4 +3] = 1.0
    img.pixels[:] = p[:]
    img.pack()
    img.use_fake_user = True
    return img

def import_ssmo(context, filepath, mat):
    # TODO: check if we can detect those pesky "NORMALS" geometry
    #       and make it easier to delete them.
    name, _ = os.path.splitext(os.path.basename(filepath))
    filedir = os.path.dirname(filepath)

    parsed = SunstormSsm.from_file(filepath)

    vertices = parsed.frames[0].vertices

    view_layer = bpy.context.view_layer
    collection = view_layer.active_layer_collection.collection

    mverts = list(map(lambda v: [v.x, v.y, v.z], vertices))
    mfaces = []
    muvs = []
    for f in parsed.faces:
        muvs.append([ f.uvs[0], f.uvs[1] ])
        muvs.append([ f.uvs[2], f.uvs[3] ])
        muvs.append([ f.uvs[4], f.uvs[5] ])

        mfaces.append([ f.indices[0], f.indices[1], f.indices[2] ])

    mesh_data = bpy.data.meshes.new(name + '_Mesh')
    mesh_data.from_pydata(mverts, [], mfaces) # [] = no edges defined
    mesh_data.update()
    #IRA: mesh_data.transform(mat)

    obj = bpy.data.objects.new(name, mesh_data)
    collection.objects.link(obj)

    for ssm_mat in parsed.materials:
        material = None
        if ssm_mat.num_skins > 0:
            skin = ssm_mat.skins[0]
            texname = parsed.textures[skin.texture_index].name.removeprefix('file;')
            material = create_material(f"{name}_{skin.name}", os.path.join(filedir, texname))
        obj.data.materials.append(material)

    # Set materials (per face)
    for face_index in range(parsed.num_faces):
        f = parsed.faces[face_index]
        obj.data.polygons[face_index].material_index = f.material_id

    uv = obj.data.uv_layers.new(name=name + "_UV")
    for loop in obj.data.loops:
        uv.data[loop.index].uv = muvs[loop.index]

    # Parse animations
    if parsed.num_animations > 0:     
        actions = []
        for anim in parsed.animations:
            action = bpy.data.actions.new(anim.name)
            fcurve = action.fcurves.new('eval_time')

            actions.append(action)

            for frame_index in anim.frame_indices:
                frame = parsed.frames[frame_index]

                sk = obj.shape_key_add(name=frame.name, from_mix=False)
                sk.interpolation = 'KEY_LINEAR'
                
                for j in range(parsed.num_vertices):
                    v = frame.vertices[j]
                    sk.data[j].co.x = v.x
                    sk.data[j].co.y = v.y
                    sk.data[j].co.z = v.z
                    #IRA: sk.data[j].co = mat @ sk.data[j].co

                fcurve.keyframe_points.insert(frame_index, sk.frame)
    
        obj.data.shape_keys.use_relative = False
        obj.data.shape_keys.animation_data_create()
        obj.data.shape_keys.animation_data.action = actions[0]
        
        anim_data = obj.data.shape_keys.animation_data
        for action in actions:
            trk = anim_data.nla_tracks.new()
            trk.name = action.name
            strip = trk.strips.new(action.name, int(action.frame_range[0]), action)
            # update start/end frames of action
            strip.action_frame_start = action.frame_range[0]
            strip.action_frame_end = action.frame_range[1]

    return {'FINISHED'}
