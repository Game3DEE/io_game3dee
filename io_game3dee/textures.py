import os
import bpy

from .kaitai.sunstorm_stx import SunstormStx

# Wrapper around bpy.data.images.load to handle custom image formats
def load_image_wrapper(path):
    name, ext = os.path.splitext(os.path.basename(path))
    match ext.lower():
        case ".stx":
            return import_sunstorm_stx(name, path)
        case _:
            return bpy.data.images.load(path)

# Called with an actual path or None if unable to find correct texture
def create_material(name, path):
    mat = bpy.data.materials.new(name=name+"_Material")
    # Only use path if it is set, and points to a loadable texture
    if path is not None and os.path.isfile(path):
        image = load_image_wrapper(path)
        if image is not None:
            mat.use_nodes = True
            texImage = bpy.data.textures.new(name+'_texture', 'IMAGE')
            texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
            texImage.image = image
            bsdf = mat.node_tree.nodes["Principled BSDF"]
            mat.node_tree.links.new(
                bsdf.inputs['Base Color'], texImage.outputs['Color'])

    return mat

# TODO: fix assumption of 24bit textures
def import_sunstorm_stx(name, path):
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
