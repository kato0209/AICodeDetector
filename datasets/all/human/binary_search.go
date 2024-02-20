func binarySearch(nums []int, value int) int {
	low := 0
	high := len(nums) - 1

	for low <= high {
		mid := (low + high) / 2

		if nums[mid] == value {
			return mid
		}
		if nums[mid] < value {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return -1
}

// 再帰を使った、バイナリサーチ
func binarySearchRecursive(nums []int, value int, low, high int) int {
	if low > high {
		return -1
	}
	mid := (low + high) / 2
	if nums[mid] == value {
		return mid
	} else if nums[mid] < value {
		return binarySearchRecursive(nums, value, mid+1, high)
	} else {
		return binarySearchRecursive(nums, value, low, mid-1)
	}
}
