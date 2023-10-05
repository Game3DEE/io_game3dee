# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Animator3df(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(4)
        if not self.magic == b"\x4B\x69\x65\x76":
            raise kaitaistruct.ValidationNotEqualError(b"\x4B\x69\x65\x76", self.magic, self._io, u"/seq/0")
        self.version = self._io.read_u4le()
        self.skipped = self._io.read_bytes(120)
        self.num_textures = self._io.read_u4le()
        self.textures = []
        for i in range(self.num_textures):
            self.textures.append((KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"utf8"))

        self.num_lods = self._io.read_u4le()
        self.lods = []
        for i in range(self.num_lods):
            self.lods.append(Animator3df.Lod(self._io, self, self._root))


    class Lod(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_vertices = self._io.read_u4le()
            self.num_faces = self._io.read_u4le()
            self.num_bones = self._io.read_u4le()
            self.vertices = []
            for i in range(self.num_vertices):
                self.vertices.append(Animator3df.Vertex(self._io, self, self._root))

            self.faces = []
            for i in range(self.num_faces):
                self.faces.append(Animator3df.Face(self._io, self, self._root))

            self.bones = []
            for i in range(self.num_bones):
                self.bones.append(Animator3df.Bone(self._io, self, self._root))

            self.texture_id_per_face = self._io.read_bytes(self.num_faces)
            self.face_by_texture_counts = []
            for i in range(self._root.num_textures):
                self.face_by_texture_counts.append(self._io.read_u4le())



    class Vertex(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()
            self.owner = self._io.read_s2le()
            self.hide = self._io.read_s2le()


    class Face(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.a = self._io.read_u2le()
            self.b = self._io.read_u2le()
            self.c = self._io.read_u2le()
            self.flags = self._io.read_u2le()
            self.tax = self._io.read_f4le()
            self.tbx = self._io.read_f4le()
            self.tcx = self._io.read_f4le()
            self.tay = self._io.read_f4le()
            self.tby = self._io.read_f4le()
            self.tcy = self._io.read_f4le()


    class Bone(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"utf8")
            self.x = self._io.read_f4le()
            self.y = self._io.read_f4le()
            self.z = self._io.read_f4le()
            self.owner = self._io.read_s2le()
            self.hide = self._io.read_s2le()



