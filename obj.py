def parse_obj_manual(filepath):
    vertices = []
    texcoords = []
    normals = []
    faces = []

    with open(filepath, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue

            prefix = parts[0]
            if prefix == 'v':
                vertices.append(list(map(float, parts[1:])))
            elif prefix == 'vt':
                texcoords.append(list(map(float, parts[1:])))
            elif prefix == 'vn':
                normals.append(list(map(float, parts[1:])))
            elif prefix == 'f':
                face_indices = []
                for p in parts[1:]:
                    # Face indices can be v, v/vt, v//vn, or v/vt/vn
                    indices = list(map(int, p.split('/')))
                    face_indices.append(indices)
                faces.append(face_indices)
    return {'vertices': vertices, 'texcoords': texcoords, 'normals': normals, 'faces': faces}

data = parse_obj_manual('cube.obj')
print('vertices' + str(data['vertices']))
print('texcoords' + str(data['texcoords']))
print('normals' + str(data['normals']))
print('faces' + str(data['faces']))