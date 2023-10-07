import os
import bpy

from bpy_extras.io_utils import ImportHelper, ExportHelper, orientation_helper, axis_conversion
from bpy.props import StringProperty, FloatProperty
from bpy.types import Operator
from mathutils import Matrix

from .actionforms import import_animator_3df
from .canopygames import import_mdl
from .darkstone import import_o3d
from .prism3d import import_gdt, import_pmd, import_pmg, import_psm
from .sunstorm import import_ssm

bl_info = {
    "name": "Import/Export for many 3D games",
    "description": "Import/Export for many 3D games",
    "author": "Ithamar R. Adema",
    "version": (1, 0, 0),
    "blender": (2, 82, 0),
    "location": "File > Import > Game3DEE",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "https://github.com/Game3DEE/io_game3dee/wiki",
    "tracker_url": "https://github.com/Game3DEE/io_game3dee/issues",
    "category": "Import-Export",
}

import_exts = [
    # ActionForms / Carnivores
    "3df", "trk",
    # Chasm
#    "3o", "car",
    # Darkstone: Evil Reigns
    "o3d",
    # Prism3D (Shark)
    "gdt", "pmd", "pmg", "psm",
    # Quickdraw3D
#    "3dmf",
    # Serious Engine (v1)
#    "ba", "bm", "bs", "mdl", "tex",
    # 
    "ssm",
    # Vivisector/..
#    "cmf",
]
def import_model(context, filepath, mat):
    _, ext = os.path.splitext(os.path.basename(filepath))
    
    match ext.lower():
        case ".mdl":
            return import_mdl(context, filepath, mat)

        case ".o3d":
            return import_o3d(context, filepath, mat)

        case ".gdt":
            return import_gdt(context, filepath, mat)
        case ".pmd":
            return import_pmd(context, filepath, mat)
        case ".pmg":
            return import_pmg(context, filepath, mat)
        case ".psm":
            return import_psm(context, filepath, mat)
        case ".3df":
            return import_animator_3df(context, filepath, mat)

        case "ssm":
            return import_ssm(context, filepath, mat)

    return {'FINISHED'}

def export_model(context, filepath, mat):
    return {'FINISHED'}

# General import / export UI handling

@orientation_helper(axis_forward='Z', axis_up='Y')
class ImportGame3DEE(Operator, ImportHelper):
    """Import of many different 3D game formats"""
    # important since its how bpy.ops.import_test.some_data is constructed
    bl_idname = "import_game3dee.some_data"
    bl_label = "Import Model"

    # ImportHelper mixin class uses this
    filename_ext = ";".join(map(lambda ext: ".%s" % ext, import_exts))
    filter_glob: StringProperty(
        default=";".join(map(lambda ext: "*.%s" % ext, import_exts)),
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    global_scale: FloatProperty(
        name="Scale",
        min=0.01, max=1000.0,
        default=1.0,
    )

    def execute(self, context):
        global_matrix = (
            Matrix.Scale(self.global_scale, 4) @
            axis_conversion(
                to_forward=self.axis_forward,
                to_up=self.axis_up,
            ).to_4x4()
        )

        return import_model(context, self.filepath, global_matrix)


# -----------------------------------------------------------------------------
# Export
# -----------------------------------------------------------------------------

def prepare_export(context, operator):
    # Exit edit mode before exporting, so current object states are exported properly.
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='OBJECT')

    # Determine object to export
    obj = context.active_object
    if obj is not None:
        if obj.type != 'MESH':
            # If an armature was selected, find corresponding mesh
            if obj.type == 'ARMATURE':
                for o in obj.children:
                    if o.type == 'MESH':
                        obj = o
                        break
                # If we didn't find a mesh, bail out
                if obj.type != 'MESH':
                    obj = None
            else:
                # neither MESH or ARMATURE, bail out
                obj = None

    # Validate selected mesh, report errors if not okay
    if obj is not None:
        mesh = obj.to_mesh()
        if mesh.uv_layers.active is None:
            operator.report({'ERROR'}, 'No UV layer found on model')
            obj.to_mesh_clear()
            return None

        obj.to_mesh_clear()
    else:
        operator.report({'ERROR'}, 'No model selected')
        return None

    return obj

@orientation_helper(axis_forward='-Z', axis_up='Y')
class ExportGame3DEE(Operator, ExportHelper):
    """Export to many 3D game formats"""
    bl_idname = "export_game3dee.some_data"
    bl_label = "Export Model (Game3DEE)"
    bl_options = {'PRESET'}

    # ExportHelper mixin class uses this
    filename_ext = ".3df"

    filter_glob: StringProperty(
        default="*.3df",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    global_scale: FloatProperty(
        name="Scale",
        min=0.01, max=1000.0,
        default=1.0,
    )

    def execute(self, context):
        obj = prepare_export(context, self)
        if obj is None:
            return {'CANCELLED'}

        global_matrix = (
            Matrix.Scale(self.global_scale, 4) @
            axis_conversion(
                to_forward=self.axis_forward,
                to_up=self.axis_up,
            ).to_4x4()
        )

        return export_model(context, self.filepath, obj, global_matrix)

def menu_func_import(self, context):
    self.layout.operator(ImportGame3DEE.bl_idname, text="Model (Game3DEE)")

def menu_func_export(self, context):
    self.layout.operator(ImportGame3DEE.bl_idname, text="Model (Game3DEE)")

def register():
    bpy.utils.register_class(ExportGame3DEE)
    bpy.utils.register_class(ImportGame3DEE)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    bpy.utils.unregister_class(ExportGame3DEE)
    bpy.utils.unregister_class(ImportGame3DEE)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
