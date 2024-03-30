# Autogenerated and manually edited file; see README.md for more details
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum

if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class AtmosfearUbfc(KaitaiStruct):

    class BlockId(Enum):
        object_start = 1
        texture_count = 2
        textures = 3
        face_count = 8209
        vert_count = 8210
        faces = 8211
        face_unkn_attr1_u4 = 8215
        face_unkn_attr6_u4 = 8218
        face_materials = 8220
        face_unkn_attr2_u4 = 8221
        uv1 = 8224
        uv2 = 8225
        vertices = 8227
        something_count = 8240
        something_unkn_attr1_2x_u4 = 8241
        something_unkn_attr2_2x_u4 = 8242
        something_unkn_attr3_v3f = 8243
        alt_faces = 8244
        header = 61441
        bone_count = 61456
        bone_names = 61457
        bone_positions = 61458
        bone_unkn_attr1_u2 = 61459
        bone_parents = 61460
        bone_transforms = 61461
        face_unkn_attr3_u4 = 61473
        face_unkn_attr4_u1 = 61474
        face_unkn_attr5_u2 = 61475
        vertex_bones = 61488
        vertex_unkn_attr1_u2 = 61489
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x55\x42\x46\x43":
            raise kaitaistruct.ValidationNotEqualError(b"\x55\x42\x46\x43", self.magic, self._io, u"/seq/0")
        self.zero1 = self._io.read_u4le()
        self.blocks = []
        i = 0
        while not self._io.is_eof():
            self.blocks.append(AtmosfearUbfc.Block(self._io, self, self._root))
            i += 1


    class Uv(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.a_u = self._io.read_f4le()
            self.b_u = self._io.read_f4le()
            self.c_u = self._io.read_f4le()
            self.d_u = self._io.read_f4le()
            self.a_v = self._io.read_f4le()
            self.b_v = self._io.read_f4le()
            self.c_v = self._io.read_f4le()
            self.d_v = self._io.read_f4le()


    class Vector3f(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()


    class SomethingUnknAttr3V3fBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.vertices = []
            i = 0
            while not self._io.is_eof():
                self.vertices.append(AtmosfearUbfc.Vector3f(self._io, self, self._root))
                i += 1



    class UvBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.uvs = []
            i = 0
            while not self._io.is_eof():
                self.uvs.append(AtmosfearUbfc.Uv(self._io, self, self._root))
                i += 1



    class HeaderBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.val1 = self._io.read_u4le()
            self.val2 = self._io.read_u4le()
            self.val3 = self._io.read_u4le()
            self.val4 = self._io.read_s4le()
            self.float1 = self._io.read_f4le()
            self.val6 = self._io.read_u4le()
            self.val7 = self._io.read_u4le()
            self.val8 = self._io.read_u4le()
            self.val9 = self._io.read_u4le()
            self.val10 = self._io.read_u4le()
            self.val11 = self._io.read_u4le()


    class VertBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.vertices = []
            i = 0
            while not self._io.is_eof():
                self.vertices.append(AtmosfearUbfc.Vector3f(self._io, self, self._root))
                i += 1



    class BoneTransformsBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bone_transforms = []
            i = 0
            while not self._io.is_eof():
                self.bone_transforms.append(AtmosfearUbfc.Matrix3x3f(self._io, self, self._root))
                i += 1



    class TexturesBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.textures = []
            i = 0
            while not self._io.is_eof():
                self.textures.append((KaitaiStream.bytes_terminate(self._io.read_bytes(128), 0, False)).decode(u"utf8"))
                i += 1



    class Face(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.a = self._io.read_u4le()
            self.b = self._io.read_u4le()
            self.c = self._io.read_u4le()
            self.d = self._io.read_u4le()


    class BonePositionsBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bone_positions = []
            i = 0
            while not self._io.is_eof():
                self.bone_positions.append(AtmosfearUbfc.Vector3f(self._io, self, self._root))
                i += 1



    class Block(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = KaitaiStream.resolve_enum(AtmosfearUbfc.BlockId, self._io.read_u4le())
            self.size = self._io.read_u4le()
            _on = self.id
            if _on == AtmosfearUbfc.BlockId.uv1:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.UvBlock(_io__raw_data, self, self._root)
            elif _on == AtmosfearUbfc.BlockId.vert_count:
                self.data = self._io.read_u4le()
            elif _on == AtmosfearUbfc.BlockId.something_count:
                self.data = self._io.read_u4le()
            elif _on == AtmosfearUbfc.BlockId.texture_count:
                self.data = self._io.read_u4le()
            elif _on == AtmosfearUbfc.BlockId.bone_names:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.BoneNamesBlock(_io__raw_data, self, self._root)
            elif _on == AtmosfearUbfc.BlockId.alt_faces:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.FacesBlock(_io__raw_data, self, self._root)
            elif _on == AtmosfearUbfc.BlockId.vertex_bones:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.VertexBonesBlock(_io__raw_data, self, self._root)
            elif _on == AtmosfearUbfc.BlockId.bone_count:
                self.data = self._io.read_u4le()
            elif _on == AtmosfearUbfc.BlockId.something_unkn_attr3_v3f:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.SomethingUnknAttr3V3fBlock(_io__raw_data, self, self._root)
            elif _on == AtmosfearUbfc.BlockId.bone_positions:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.BonePositionsBlock(_io__raw_data, self, self._root)
            elif _on == AtmosfearUbfc.BlockId.textures:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.TexturesBlock(_io__raw_data, self, self._root)
            elif _on == AtmosfearUbfc.BlockId.face_count:
                self.data = self._io.read_u4le()
            elif _on == AtmosfearUbfc.BlockId.face_materials:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.FaceMaterialsBlock(_io__raw_data, self, self._root)
            elif _on == AtmosfearUbfc.BlockId.header:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.HeaderBlock(_io__raw_data, self, self._root)
            elif _on == AtmosfearUbfc.BlockId.uv2:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.UvBlock(_io__raw_data, self, self._root)
            elif _on == AtmosfearUbfc.BlockId.bone_transforms:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.BoneTransformsBlock(_io__raw_data, self, self._root)
            elif _on == AtmosfearUbfc.BlockId.faces:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.FacesBlock(_io__raw_data, self, self._root)
            elif _on == AtmosfearUbfc.BlockId.bone_parents:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.BoneParentsBlock(_io__raw_data, self, self._root)
            elif _on == AtmosfearUbfc.BlockId.vertices:
                self._raw_data = self._io.read_bytes(self.size)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = AtmosfearUbfc.VertBlock(_io__raw_data, self, self._root)
            else:
                self.data = self._io.read_bytes(self.size)


    class BoneNamesBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bone_names = []
            i = 0
            while not self._io.is_eof():
                self.bone_names.append((KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"utf8"))
                i += 1



    class Matrix3x3f(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.elements = []
            for i in range(9):
                self.elements.append(self._io.read_f4le())



    class FacesBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.faces = []
            i = 0
            while not self._io.is_eof():
                self.faces.append(AtmosfearUbfc.Face(self._io, self, self._root))
                i += 1



    class VertexBonesBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bone_indices = []
            i = 0
            while not self._io.is_eof():
                self.bone_indices.append(self._io.read_u2le())
                i += 1



    class FaceMaterialsBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.indices = []
            i = 0
            while not self._io.is_eof():
                self.indices.append(self._io.read_u4le())
                i += 1



    class BoneParentsBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.bone_parents = []
            i = 0
            while not self._io.is_eof():
                self.bone_parents.append(self._io.read_s2le())
                i += 1



