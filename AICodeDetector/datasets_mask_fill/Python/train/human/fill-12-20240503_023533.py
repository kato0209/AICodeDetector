# Python program to find the first present element x
# in a sorted array using Exponential Search

# A recursive binary search function returns 
# location of the element x
# in the given array arr[l..r] is 
# present at (l,r), otherwise -1
def binarySearch( arr, l, r, x):
	if r >= l:
		mid = l + ( r-l ) // 2
		
		# If the element is at 
		# the middle itself
		if arr[mid] == x:
			return mid
		
		# If the element is smaller than mid, 
		# then the element can only be present in # the left subarray
		if arr[mid] > x:
			return binarySearch(arr, l, 
								mid , x)
		
		# Else he element can only be
		# present in the right
		return binarySearch(arr, mid + 1, r, x)
		
	# We reach here if the element is not present
	return -1

# Returns the position of first
# occurrence of x in array
def