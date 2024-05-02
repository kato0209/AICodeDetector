def Sequential_Search(dlist, item):

    pos = 0
    found = False
 <extra_id_0>  <extra_id_1>   while pos < len(dlist) and not <extra_id_2>    <extra_id_3>  if dlist[pos] == item:
   <extra_id_4>        found = True
        else:
 <extra_id_5>          pos = pos + 1
    
    return found, pos

print(Sequential_Search([11,23,58,31,56,77,43,12,65,19],31))
