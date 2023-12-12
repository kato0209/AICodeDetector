def matrix_multiply(matrix1, matrix2):
    """
    Multiply two matrices.
    
    :param matrix1: First matrix as a list of lists.
    :param matrix2: Second matrix as a list of lists.
    :return: The product of the two matrices as a list of lists.
    """
    # Number of rows and columns in the matrices
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    # Check if multiplication is possible
    if cols_matrix1 != rows_matrix2:
        raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    # Perform multiplication
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Example matrices
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[2, 0], [1, 2]]

# Multiply the matrices
result_matrix = matrix_multiply(matrix1, matrix2)
result_matrix  # This should return the product of matrix1 and matrix2

