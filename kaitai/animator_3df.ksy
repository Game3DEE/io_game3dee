meta:
  id: animator_3df
  file-extension: 3df
  application: ActionForms Animator software & games
  endian: le
  encoding: utf8
  license: CC0

seq:
  - id: magic
    contents: "Kiev"
  - id: version
    type: u4
    valid:
      any-of: [4, 6]
    doc: |
      V4 is used in Duke Nukem: Endangered Species, V6 is current Animator format.
  - id: skipped
    size: 120
  - id: num_textures
    type: u4
  - id: textures
    type: strz
    size: 16
    repeat: expr
    repeat-expr: num_textures
  - id: num_lods
    type: u4
  - id: lods
    type: lod
    repeat: expr
    repeat-expr: num_lods
    
types:
  lod:
    seq:
      - id: num_vertices
        type: u4
      - id: num_faces
        type: u4
      - id: num_bones
        type: u4
      - id: vertices
        type: vertex
        repeat: expr
        repeat-expr: num_vertices
      - id: faces
        type: face
        repeat: expr
        repeat-expr: num_faces
      - id: bones
        type: bone
        repeat: expr
        repeat-expr: num_bones
      - id: texture_id_per_face
        size: num_faces
      - id: face_by_texture_counts
        type: u4
        repeat: expr
        repeat-expr: _root.num_textures
  
  vertex:
    seq:
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
      - id: owner
        type: s2
      - id: hide
        type: s2

  face:
    seq:
      - id: a
        type: u2
      - id: b
        type: u2
      - id: c
        type: u2
      - id: flags
        type:
          switch-on: _root.version
          cases:
            4: u2
            6: u4
      - id: tax
        type: f4
      - id: tbx
        type: f4
      - id: tcx
        type: f4
      - id: tay
        type: f4
      - id: tby
        type: f4
      - id: tcy
        type: f4

  bone:
    seq:
      - id: name
        type: strz
        size: 32
      - id: x
        type: f4
      - id: y
        type: f4
      - id: z
        type: f4
      - id: owner
        type: s2
        doc: Parent bone, or -1 if no parent
      - id: hide
        type: s2