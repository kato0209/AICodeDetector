# Method to find an element in a sorted array using binary search.
# A recursive binary search function returns 
# location of x in given array arr[l..r] is 
# present, otherwise it returns -1.
def binarySearch( arr, l, r, x):
	while r >= l:
		mid = l + ( r-l ) // 2
		
		# If the element is present at 
		# the middle itself
		if arr[mid] == x:
			return mid
		
		# If the element is smaller than mid, # it can only be present in the 
		# left subarray
		if arr[mid] > x:
			return binarySearch(arr, l, 
								mid - 1, x)
		
		# Otherwise, element can only be
		# present in the right
		return binarySearch(arr, mid + 1, r, x)
		
	# We reach here if the element is not present
	return -1

# Returns the position of first
# occurrence of x in array
def