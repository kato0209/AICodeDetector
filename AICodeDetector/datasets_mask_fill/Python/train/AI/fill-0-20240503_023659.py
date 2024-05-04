def levenshtein_distance(str1, str2):
    """
   Calculate the levenshtein distance between two strings.
    """
    # Size of the matrix
    rows = len(str1) + 1   cols = len(str2) + 1

   # Initialize the matrix
    dist = [[1 for _ in range(cols)] for _ in range(rows)]    # Populate the matrix
    for i in range(1, rows):
        dist[0][i] = i
    for j in range(1, cols):
       dist[0][j] = j

    # Calculate distances
    for i in range(1, rows):
     