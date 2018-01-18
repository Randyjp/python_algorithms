def matrix_zeros(matrix):
    number_rows = len(matrix)
    number_columns = len(matrix[0])

    row_zeros = [False for x in range(number_rows)]
    col_zeros = [False for x in range(number_columns)]

    for i in range(number_rows):
        for j in range(number_columns):
            if matrix[i][j] == 0:
                row_zeros[i] = True
                col_zeros[j] = True

    null_rows(matrix, number_rows, number_columns, row_zeros)
    null_cols(matrix, number_rows, number_columns, col_zeros)

    return matrix


def null_rows(matrix, number_rows, number_columns, row_zeros):
    for i in range(number_rows):
        if row_zeros[i]:
            for j in range(number_columns):
                matrix[i][j] = 0


def null_cols(matrix, number_rows, number_columns, col_zeros):
    for j in range(number_columns):
        if col_zeros[j]:
            for i in range(number_rows):
                matrix[i][j] = 0


print matrix_zeros([[2, 1], [3, 0], [8, 8], [6, 2]])
