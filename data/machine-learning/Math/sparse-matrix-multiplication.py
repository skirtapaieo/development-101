def sparse_matrix_multiplication(matrix_a, matrix_b):
    # First, we need to check if the matrices can be multiplied together.
    # This can be done by comparing the number of columns in matrix_a 
    # with the number of rows in matrix_b.
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    
    # Initialize result matrix with zeros
    result = [[0]*len(matrix_b[0]) for _ in range(len(matrix_a))]

    # Now, for each row in matrix_a, we consider only non-zero elements
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            if matrix_a[i][j] != 0:  # This is our sparse condition
                # And for each column in matrix_b, again we consider only non-zero elements
                for k in range(len(matrix_b[0])):
                    if matrix_b[j][k] != 0:
                        result[i][k] += matrix_a[i][j] * matrix_b[j][k]
    return result
