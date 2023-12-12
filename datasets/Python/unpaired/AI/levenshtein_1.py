def levenshtein_distance(str1, str2):
    """
    Calculate the Levenshtein distance between two strings.
    """
    # Size of the matrix
    rows = len(str1) + 1
    cols = len(str2) + 1

    # Initialize the matrix
    dist = [[0 for _ in range(cols)] for _ in range(rows)]

    # Populate the matrix
    for i in range(1, rows):
        dist[i][0] = i
    for j in range(1, cols):
        dist[0][j] = j

    # Calculate distances
    for i in range(1, rows):
        for j in range(1, cols):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1

            dist[i][j] = min(dist[i - 1][j] + 1,      # Deletion
                             dist[i][j - 1] + 1,      # Insertion
                             dist[i - 1][j - 1] + cost)  # Substitution

    return dist[-1][-1]

# Example usage
levenshtein_example = levenshtein_distance("kitten", "sitting")
levenshtein_example  # This should return the Levenshtein distance between "kitten" and "sitting"

