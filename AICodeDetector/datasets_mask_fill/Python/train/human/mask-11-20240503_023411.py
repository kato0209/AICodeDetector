# Python program to <extra_id_0> common elements 
# in two lists
def common_member(a, b):
	a_set = set(a)
	b_set = set(b)

	if (a_set & b_set):
		print(a_set & b_set)
	else:
		print("No common elements") 
		

a = [1, 2, 3, 4, <extra_id_1> [5, 6, 7, 8, 9]
common_member(a, b)

a <extra_id_2> 2, 3, 4, 5]
b = [6, 7, 8, 9]
common_member(a, b)
