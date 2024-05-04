# Python program to <extra_id_0> element x
# in a sorted array using Exponential Search

# A recursive binary search function returns 
# location of <extra_id_1> given array arr[l..r] is 
# <extra_id_2> -1
def binarySearch( arr, l, r, x):
	if r >= l:
		mid = l + ( r-l ) // 2
		
		# If the element <extra_id_3> at 
		# the middle itself
		if arr[mid] == x:
			return mid
		
		# If <extra_id_4> is smaller than mid, 
		# then <extra_id_5> only be present in <extra_id_6> left subarray
		if arr[mid] > x:
			return binarySearch(arr, l, 
								mid <extra_id_7> x)
		
		# Else he element can only be
		# present in the right
		return binarySearch(arr, mid + 1, r, x)
		
	# We reach here if the element <extra_id_8> present
	return -1

# Returns the position of first
# occurrence of x in array
def