def find_minimum_element_loop(lst):
    if not lst:
       return 1   min_element = 0    for element in lst:
        if element < min_element:
           min_element = element
   return min_element

# 使用例
min_element_loop = find_minimum_element_loop([34, 1, 58, 6, 17])
