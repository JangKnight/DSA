def dir_reduc(arr):
    opposite = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    true_dir = []
    
    for direction in arr:
        if true_dir and true_dir[-1] == opposite[direction]:
            true_dir.pop()
        else:
            true_dir.append(direction)
    
    return true_dir