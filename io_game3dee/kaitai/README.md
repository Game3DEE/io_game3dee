# Kaitai files

The files in this directory are the kaitai runtime module and parsers generated by the kaitai struct compiler.

To be able to use the kaitai struct compiler output, the following modifications were made to it to use the local kaitai module:

from:

```
# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
```

to:

```
# Autogenerated and manually edited file; see README.md for more details
from . import kaitaistruct
from .kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
```

this imports the same symbols, just from the local kaitai module instead of a systemwide one.
