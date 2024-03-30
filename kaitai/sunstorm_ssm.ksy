meta:
  id: sunstorm_ssm
  title: Sunstorm Model Format
  application: SunStorm games from ~y2k, e.g. PrimalPrey, Deer Hunter 3, etc.
  license: CC0-1.0
  file-extension: ssm
  endian: le
  encoding: utf8

seq:
  - contents: "SSMO"
  - id: version
    type: u4
    valid: 1
    doc: Format version; only 1 is currently known to exist.

  - id: num_vertices
    type: u2
  - id: num_faces
    type: u2
  - id: num_textures
    type: u2
  - id: num_frames
    type: u2
    doc: Total number of frames across all animations.
  - id: num_animations
    type: u2
  - id: num_materials
    type: u2
  - id: num_metadata
    type: u2

  - id: faces
    type: face
    repeat: expr
    repeat-expr: num_faces

  - id: textures
    type: texture
    repeat: expr
    repeat-expr: num_textures

  - id: frames
    type: frame
    repeat: expr
    repeat-expr: num_frames

  - id: animations
    type: animation
    repeat: expr
    repeat-expr: num_animations

  - id: materials
    type: material
    repeat: expr
    repeat-expr: num_materials

  - id: metadata
    type: metadata
    repeat: expr
    repeat-expr: num_metadata

types:
  face:
    seq:
      - id: indices
        type: u2
        repeat: expr
        repeat-expr: 3
        doc: Vertex indices for this face
      - id: flags
        type: u2
      - id: uvs
        type: f4
        repeat: expr
        repeat-expr: 3 * 2
        doc: UV coordinates for the 3 vertices in this face
      - id: material_id
        type: u2
      - id: unknown
        type: u2

  texture:
    seq:
      - id: filler
        size: 4
      - id: name_len
        type: u2
      - id: name
        type: str
        size: name_len

  frame:
    seq:
      - id: filler1
        contents: [ 0,0,0,0 ]
      - id: filler2
        contents: [ 0,0,0,0 ]
      - id: name_len
        type: u2
      - id: name
        type: str
        size: name_len
      - id: per_material
        type: u1
        repeat: expr
        repeat-expr: _root.num_materials
      - id: vertices
        type: vector3f
        repeat: expr
        repeat-expr: _root.num_vertices

  animation:
    seq:
      - id: filler1
        contents: [ 0,0,0,0 ]
      - id: filler2
        contents: [ 0,0,0,0 ]
      - id: num_frame_indices
        type: u2
      - id: name_len
        type: u2
      - id: name
        type: str
        size: name_len
      - id: frame_indices
        type: u2
        repeat: expr
        repeat-expr: num_frame_indices
      - id: frame_durations
        type: f4
        repeat: expr
        repeat-expr: num_frame_indices

  material:
    seq:
      - id: filler1
        type: u4
      - id: filler2
        type: u4
      - id: name_len
        type: u2
      - id: name
        type: str
        size: name_len
      - id: num_skins
        type: u2
      - id: skins
        type: skin
        repeat: expr
        repeat-expr: num_skins
      - id: num_metadata
        type: u2
      - id: metadata
        type: metadata
        repeat: expr
        repeat-expr: num_metadata

  skin:
    seq:
      - id: texture_index
        type: u2
      - id: name_len
        type: u2
      - id: name
        type: str
        size: name_len

  metadata:
    seq:
      - id: filler
        contents: [ 0 ]
      - id: key_len
        type: u2
      - id: key
        type: str
        size: key_len
      - id: value_len
        type: u2
      - id: value
        type: str
        size: value_len

  vector3f:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
