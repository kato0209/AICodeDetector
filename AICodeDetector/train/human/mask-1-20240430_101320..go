func binary_search(array []int64, to_search int64) bool {
	found := false
	low := 0
	high := len(array) - 1
	for low <= high {
	 <extra_id_0> := (low + high) / 2
	  if array[mid] == to_search {
		found = <extra_id_1> }
	  if <extra_id_2> to_search {
		high = mid - 1
	  } else {
		low = mid + 1
	  <extra_id_3>  }
