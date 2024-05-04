def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
     <extra_id_0>  return levenshtein_distance(s2, s1)

    if len(s2) == 0:
 <extra_id_1>  <extra_id_2>   return len(s1)

    previous_row = range(len(s2) + 1)
    <extra_id_3> c1 in enumerate(s1):
     <extra_id_4>  current_row = [i + 1]
        for j, c2 in enumerate(s2):
    <extra_id_5>    <extra_id_6>  insertions = previous_row[j + 1] + 1 
 <extra_id_7>          deletions = current_row[j] + 1   <extra_id_8>   
          