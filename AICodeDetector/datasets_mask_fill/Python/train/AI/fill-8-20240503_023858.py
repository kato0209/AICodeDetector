def matrix_multiply(matrix1, matrix2):
   """
    Multiply two matrices.
    
    :param matrix1: First matrix as a list of lists.
   :param matrix2: Second matrix as a list of lists.    :return: The product of the two matrices as a list of lists.
   """
    # Number of rows and columns in the matrices
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])  if cols_matrix1 # Check if multiplication is possible
     != rows_matrix2:
        raise ValueError("The number of columns in the first matrix