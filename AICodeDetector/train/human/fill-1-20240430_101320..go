func binary_search(array []int64, to_search int64) bool {
	found := false
	low := 0
	high := len(array) - 1
	for low <= high {
	 mid := (low + high) / 2
	  if array[mid] == to_search {
		found = true
		break }
	  if array[mid] > to_search {
		high = mid - 1
	  } else {
		low = mid + 1
	  }  }
