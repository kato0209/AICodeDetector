# <extra_id_0> to find an element <extra_id_1> a sorted array using <extra_id_2> A recursive binary search function returns 
# location of x in given array arr[l..r] is 
# present, otherwise <extra_id_3> arr, l, <extra_id_4> r >= l:
		mid = l + ( r-l ) // 2
		
		# If the element is present at 
		# the middle itself
		if arr[mid] == x:
			return mid
		
		# If the element is smaller than mid, <extra_id_5> it can only <extra_id_6> in the 
		# left subarray
		if arr[mid] > x:
			return binarySearch(arr, l, 
								mid - 1, x)
		
		# <extra_id_7> element can only be
		# present in the right
		return binarySearch(arr, mid + 1, <extra_id_8> We reach here if the element is not present
	return -1

# Returns the position of first
# occurrence of x in array
def