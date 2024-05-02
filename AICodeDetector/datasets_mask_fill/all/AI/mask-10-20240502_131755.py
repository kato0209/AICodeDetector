def matrix_multiply(matrix1, matrix2):
   <extra_id_0>    Multiply two matrices.
    
    :param matrix1: First matrix as a list of lists.
    :param matrix2: Second matrix as <extra_id_1> of <extra_id_2>   :return: The product of the two <extra_id_3> a list of lists.
    """
    # Number of rows and columns <extra_id_4> matrices
    rows_matrix1 = <extra_id_5>   cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
 <extra_id_6>  cols_matrix2 = len(matrix2[0])

    # Check if multiplication is possible
   <extra_id_7> cols_matrix1 != rows_matrix2:
        raise ValueError("The number of columns <extra_id_8> first matrix