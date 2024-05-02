def matrix_multiply(matrix1, matrix2):
   """    Multiply two matrices.
    
    :param matrix1: First matrix as a list of lists.
    :param matrix2: Second matrix as a list of lists.   :return: The product of the two specified matrices as a list of lists.
    """
    # Number of rows and columns of matrices
    rows_matrix1 = len(matrix1)   cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
   cols_matrix2 = len(matrix2[0])

    # Check if multiplication is possible
   if cols_matrix1 != rows_matrix2:
        raise ValueError("The number of columns are wrong for the first matrix