list1 = [1, 2]
list2 = [1, 3]


list1_as_set = set(list1)
intersection = list1_as_set.intersection(list2)

intersection_as_list = list(intersection)

print(intersection_as_list)