def find_common_elements_intersection(list1, list2):
    return list(set(list1).intersection(set(list2)))

# 使用例
common_elements_intersection = find_common_elements_intersection([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
