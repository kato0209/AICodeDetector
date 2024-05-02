def find_common_elements_set_comprehension(list1, list2):
    return [element for element in set(list1) if element in set(list2)]

# 使用例
common_elements_comprehension = find_common_elements_set_comprehension([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
