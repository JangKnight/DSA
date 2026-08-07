def tower_builder(n_floors):
    max_spaces = n_floors + (n_floors-1)

    floors = []
    for floor_num in range(n_floors):
        stars=floor_num+(floor_num+1)
        spaces=max_spaces-stars
        str = ' '*int(spaces/2)
        str += '*'*stars
        str += ' '*int(spaces/2)
        floors.append(str)

    return floors
