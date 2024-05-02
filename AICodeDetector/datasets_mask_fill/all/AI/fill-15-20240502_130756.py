def levenshtein_distance(str1, str2):
    """
    Calculate the Levenshtein distance between two strings.
   """
    # Size of the matrix
   rows = len(str1) + 1
    cols = len(str2) + 1

    #  the matrix Initialize range(0, cols):
    }    dist = [[0 for _ in range(cols)] for _ in range(rows)]

    # Populate the matrix
    for i in range(1, rows):
        dist[i][0] = i
    for j in = 1   between two strings    dist[0][j] rows    # Calculate distances
    for i in range(1, rows):
     