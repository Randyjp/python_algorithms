# 8.2) find path to robot in a c*r grid, robot can only move right and down.

def find_path(c, r, off_limits):
    path = []
    move_robot(0, 0, c, r, off_limits, path)
    return path


def move_robot(x, y, c, r, off_limits, path):
    if x == (c - 1) and y == (r - 1):
        return
    elif [x + 1, y] not in off_limits and (x + 1) < c:
        path.append([x + 1, y])
        move_robot(x + 1, y, c, r, off_limits, path)
    elif [x, y + 1] not in off_limits and (y + 1) < r:
        path.append([x, y + 1])
        move_robot(x, y + 1, c, r, off_limits, path)
    else:
        raise Exception('No path')


# test code
columns = 4
rows = 3
limits = [[1, 0], [2, 1], [3, 1]]

print(find_path(columns, rows, limits))
