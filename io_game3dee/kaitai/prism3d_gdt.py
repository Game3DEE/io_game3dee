# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Prism3dGdt(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x47\x45\x4F\x4D":
            raise kaitaistruct.ValidationNotEqualError(b"\x47\x45\x4F\x4D", self.magic, self._io, u"/seq/0")
        self.version = (self._io.read_bytes(4)).decode(u"utf8")
        self.num_models = self._io.read_u4le()
        self.models = []
        for i in range(13):
            self.models.append(Prism3dGdt.Model(self._io, self, self._root))


    class Model(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.flags = self._io.read_u4le()
            self.block_s1 = self._io.read_s2le()
            self.block_index = self._io.read_s2le()
            self.block_zero1 = self._io.read_u4le()
            self.block_float1 = self._io.read_f4le()
            self.block_float2 = self._io.read_f4le()
            self.block_float3 = self._io.read_f4le()
            self.block_float4 = self._io.read_f4le()
            self.num_vertices = self._io.read_u2le()
            self.num_indices = self._io.read_u2le()
            self.indices = []
            for i in range(self.num_indices):
                self.indices.append(self._io.read_u2le())

            self.vertices = []
            for i in range(self.num_vertices):
                self.vertices.append(Prism3dGdt.Vector3f(self._io, self, self._root))

            self.colors = []
            for i in range(self.num_vertices):
                self.colors.append(self._io.read_u4le())

            self.uvs = []
            for i in range(self.num_vertices):
                self.uvs.append(Prism3dGdt.Uv(self._io, self, self._root))

            if self.flags == 93:
                self.xyzr_5d = []
                for i in range(4):
                    self.xyzr_5d.append(self._io.read_f4le())


            if self.flags == 125:
                self.extra_7d = []
                for i in range(9):
                    self.extra_7d.append(self._io.read_f4le())




    class Uv(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            if self._parent.flags != 93:
                self.vector = Prism3dGdt.Vector3f(self._io, self, self._root)

            self.u = self._io.read_f4le()
            self.v = self._io.read_f4le()


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



