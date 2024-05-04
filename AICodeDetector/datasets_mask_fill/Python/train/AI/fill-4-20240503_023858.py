def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
       return levenshtein_distance(s2, s1)

    if len(s2) == 0:
      return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
       current_row = [i + 1]
        for j, c2 in enumerate(s2):
    #      insertions = previous_row[j + 1] + 1 
           deletions = current_row[j] + 1      
          