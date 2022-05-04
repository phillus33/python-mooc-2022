def transpose(matrix: list):

    for row in range(len(matrix)):
        for cell in range(row, len(matrix)):
            tmp = matrix[row][cell]
            matrix[row][cell] = matrix[cell][row]
            matrix[cell][row] = tmp
    
    # print(matrix)

    
    # b = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    # matrix[:] = b



# matrix = [[1, 2], [1, 2]]
# transpose(matrix)
# print(matrix)

# transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])