def matrix_multiply(matrix1, matrix2):
  <extra_id_0> """
    Multiply two matrices.
    
    <extra_id_1> First matrix as a list of lists.
  <extra_id_2> :param matrix2: Second matrix as a list <extra_id_3>    :return: The product of the two <extra_id_4> a list of lists.
  <extra_id_5> """
    # Number of rows and columns in the matrices
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 <extra_id_6>  <extra_id_7> # Check if multiplication is possible
    <extra_id_8> != rows_matrix2:
        raise ValueError("The number of columns in the first matrix