import os
import bpy

from .sunstorm import import_stx

# Wrapper around bpy.data.images.load to handle custom image formats
def load_image_wrapper(path):
    name, ext = os.path.splitext(os.path.basename(path))
    match ext.lower():
        case ".stx":
            return import_stx(name, path)
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
