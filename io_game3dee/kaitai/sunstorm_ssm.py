# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SunstormSsm(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._unnamed0 = self._io.read_bytes(4)
        if not self._unnamed0 == b"\x53\x53\x4D\x4F":
            raise kaitaistruct.ValidationNotEqualError(b"\x53\x53\x4D\x4F", self._unnamed0, self._io, u"/seq/0")
        self.version = self._io.read_u4le()
        if not self.version == 1:
            raise kaitaistruct.ValidationNotEqualError(1, self.version, self._io, u"/seq/1")
        self.num_vertices = self._io.read_u2le()
        self.num_faces = self._io.read_u2le()
        self.num_textures = self._io.read_u2le()
        self.num_frames = self._io.read_u2le()
        self.num_animations = self._io.read_u2le()
        self.num_materials = self._io.read_u2le()
        self.num_metadata = self._io.read_u2le()
        self.faces = []
        for i in range(self.num_faces):
            self.faces.append(SunstormSsm.Face(self._io, self, self._root))

        self.textures = []
        for i in range(self.num_textures):
            self.textures.append(SunstormSsm.Texture(self._io, self, self._root))

        self.frames = []
        for i in range(self.num_frames):
            self.frames.append(SunstormSsm.Frame(self._io, self, self._root))

        self.animations = []
        for i in range(self.num_animations):
            self.animations.append(SunstormSsm.Animation(self._io, self, self._root))

        self.materials = []
        for i in range(self.num_materials):
            self.materials.append(SunstormSsm.Material(self._io, self, self._root))

        self.metadata = []
        for i in range(self.num_metadata):
            self.metadata.append(SunstormSsm.Metadata(self._io, self, self._root))


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


    class Frame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.filler1 = self._io.read_bytes(4)
            if not self.filler1 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.filler1, self._io, u"/types/frame/seq/0")
            self.filler2 = self._io.read_bytes(4)
            if not self.filler2 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.filler2, self._io, u"/types/frame/seq/1")
            self.name_len = self._io.read_u2le()
            self.name = (self._io.read_bytes(self.name_len)).decode(u"utf8")
            self.per_material = []
            for i in range(self._root.num_materials):
                self.per_material.append(self._io.read_u1())

            self.vertices = []
            for i in range(self._root.num_vertices):
                self.vertices.append(SunstormSsm.Vector3f(self._io, self, self._root))



    class Face(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.indices = []
            for i in range(3):
                self.indices.append(self._io.read_u2le())

            self.flags = self._io.read_u2le()
            self.uvs = []
            for i in range((3 * 2)):
                self.uvs.append(self._io.read_f4le())

            self.material_id = self._io.read_u2le()
            self.unknown = self._io.read_u2le()


    class Animation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.filler1 = self._io.read_bytes(4)
            if not self.filler1 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.filler1, self._io, u"/types/animation/seq/0")
            self.filler2 = self._io.read_bytes(4)
            if not self.filler2 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.filler2, self._io, u"/types/animation/seq/1")
            self.num_frame_indices = self._io.read_u2le()
            self.name_len = self._io.read_u2le()
            self.name = (self._io.read_bytes(self.name_len)).decode(u"utf8")
            self.frame_indices = []
            for i in range(self.num_frame_indices):
                self.frame_indices.append(self._io.read_u2le())

            self.frame_durations = []
            for i in range(self.num_frame_indices):
                self.frame_durations.append(self._io.read_f4le())



    class Metadata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.filler = self._io.read_bytes(1)
            if not self.filler == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.filler, self._io, u"/types/metadata/seq/0")
            self.key_len = self._io.read_u2le()
            self.key = (self._io.read_bytes(self.key_len)).decode(u"utf8")
            self.value_len = self._io.read_u2le()
            self.value = (self._io.read_bytes(self.value_len)).decode(u"utf8")


    class Material(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.filler1 = self._io.read_u4le()
            self.filler2 = self._io.read_u4le()
            self.name_len = self._io.read_u2le()
            self.name = (self._io.read_bytes(self.name_len)).decode(u"utf8")
            self.num_skins = self._io.read_u2le()
            self.skins = []
            for i in range(self.num_skins):
                self.skins.append(SunstormSsm.Skin(self._io, self, self._root))

            self.num_metadata = self._io.read_u2le()
            self.metadata = []
            for i in range(self.num_metadata):
                self.metadata.append(SunstormSsm.Metadata(self._io, self, self._root))



    class Texture(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.filler = self._io.read_bytes(4)
            self.name_len = self._io.read_u2le()
            self.name = (self._io.read_bytes(self.name_len)).decode(u"utf8")


    class Skin(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.texture_index = self._io.read_u2le()
            self.name_len = self._io.read_u2le()
            self.name = (self._io.read_bytes(self.name_len)).decode(u"utf8")



