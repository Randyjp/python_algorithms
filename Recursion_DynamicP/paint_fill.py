# 8.10) Implement a function to fill a matrix with a new color given a point and the matrix

def paint_fill(matrix, y, x, new_color):
    # print(x, y)
    len_x = len(matrix[0]) - 1
    len_y = len(matrix[0][0]) - 1

    if y < 0 or y > len_y or x < 0 or x > len_x:
        return
    if matrix[y][x] == new_color:
        return
    # set new color
    matrix[y][x] = new_color

    # call all adjacent points
    paint_fill(matrix, y - 1, x, new_color)
    paint_fill(matrix, y + 1, x, new_color)
    paint_fill(matrix, y, x + 1, new_color)
    paint_fill(matrix, y, x - 1, new_color)


#test code
w, h = 8, 5
Matrix = [['#fff' for x in range(w)] for y in range(h)]
paint_fill(Matrix, 2, 3, '#xoxo')
print(Matrix)
