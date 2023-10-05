# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class SunstormStx(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._unnamed0 = self._io.read_bytes(4)
        if not self._unnamed0 == b"\x53\x54\x45\x58":
            raise kaitaistruct.ValidationNotEqualError(b"\x53\x54\x45\x58", self._unnamed0, self._io, u"/seq/0")
        self.val1 = self._io.read_u4le()
        self.val2 = self._io.read_u4le()
        self.val3 = self._io.read_u4le()
        self.width = self._io.read_u4le()
        self.height = self._io.read_u4le()
        self.num_mipmaps = self._io.read_u4le()
        self.val4 = self._io.read_u4le()
        self.num_metadata = self._io.read_u4le()
        self.num_uv_sets = self._io.read_u4le()
        if self.val4 != 0:
            self._unnamed10 = self._io.read_bytes(4)
            if not self._unnamed10 == b"\x53\x54\x45\x58":
                raise kaitaistruct.ValidationNotEqualError(b"\x53\x54\x45\x58", self._unnamed10, self._io, u"/seq/10")

        self.metadata = []
        for i in range(self.num_metadata):
            self.metadata.append(SunstormStx.Metadata(self._io, self, self._root))

        self.uv_sets = []
        for i in range(self.num_uv_sets):
            self.uv_sets.append(SunstormStx.UvSet(self._io, self, self._root))

        self.format_len = self._io.read_u2le()
        self.format = (self._io.read_bytes(self.format_len)).decode(u"utf8")
        self.pix_width = self._io.read_u4le()
        self.pix_height = self._io.read_u4le()
        self.pix_rgb_bitdepth = self._io.read_u4le()
        self.pix_alpha_bitdepth = self._io.read_u4le()
        self.pix_bytes_per_pixel = self._io.read_u4le()
        self.pix_num_mipmaps = self._io.read_u4le()
        self.pix_val1 = self._io.read_u4le()
        self.pix__red_bits = self._io.read_u4le()
        self.pix_green_bits = self._io.read_u4le()
        self.pix_blue_bits = self._io.read_u4le()
        self.pix_alpha_bits = self._io.read_u4le()
        self.pix_red_shift = self._io.read_u4le()
        self.pix_green_shift = self._io.read_u4le()
        self.pix_blue_shift = self._io.read_u4le()
        self.pix_alpha_shift = self._io.read_u4le()
        self.pix_red_mask = self._io.read_u4le()
        self.pix_green_mask = self._io.read_u4le()
        self.pix_blue_mask = self._io.read_u4le()
        self.pix_alpha_mask = self._io.read_u4le()
        self.pix_pixel_mask = self._io.read_u4le()
        self.pix_val15 = self._io.read_u4le()
        self.pix_val16 = self._io.read_u4le()
        self.palette = self._io.read_bytes((256 * 4))
        self.num_mipmap_metadata = self._io.read_u2le()
        self.mipmap_metadata = []
        for i in range(self.num_mipmap_metadata):
            self.mipmap_metadata.append(SunstormStx.Metadata(self._io, self, self._root))

        self.mipmaps = []
        for i in range(self.num_mipmaps):
            self.mipmaps.append(SunstormStx.Mipmap(self._io, self, self._root))


    class Metadata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.key_len = self._io.read_u2le()
            self.key = (self._io.read_bytes(self.key_len)).decode(u"utf8")
            self.value_len = self._io.read_u2le()
            self.value = (self._io.read_bytes(self.value_len)).decode(u"utf8")


    class UvSet(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown = self._io.read_u2le()
            self.num_uv_pairs = self._io.read_u2le()
            self.num_metadata = self._io.read_u2le()
            self.uvs = []
            for i in range((self.num_uv_pairs * 2)):
                self.uvs.append(self._io.read_f4le())

            self.metadata = []
            for i in range(self.num_metadata):
                self.metadata.append(SunstormStx.Metadata(self._io, self, self._root))



    class Mipmap(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.width = self._io.read_u4le()
            self.height = self._io.read_u4le()
            self.val1 = self._io.read_u4le()
            self.val2 = self._io.read_u4le()
            self.val3 = self._io.read_u4le()
            self.val4 = self._io.read_u4le()
            self.val5 = self._io.read_u4le()
            self.offset_rgb = self._io.read_u4le()
            self.offset_alpha = self._io.read_u4le()

        @property
        def rgb(self):
            if hasattr(self, '_m_rgb'):
                return self._m_rgb

            if self.offset_rgb != 4294967295:
                _pos = self._io.pos()
                self._io.seek(self.offset_rgb)
                self._m_rgb = self._io.read_bytes(((3 * self.width) * self.height))
                self._io.seek(_pos)

            return getattr(self, '_m_rgb', None)

        @property
        def alpha(self):
            if hasattr(self, '_m_alpha'):
                return self._m_alpha

            if self.offset_alpha != 4294967295:
                _pos = self._io.pos()
                self._io.seek(self.offset_alpha)
                self._m_alpha = self._io.read_bytes((self.width * self.height))
                self._io.seek(_pos)

            return getattr(self, '_m_alpha', None)



