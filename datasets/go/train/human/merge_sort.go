func main() {
	array := []int{4, 9, 1, 3, 5, 7, 6, 10, 8, 2}
	sorted := mergeSort(array)
	fmt.Println(sorted)
}
func mergeSort(array []int) []int {
	if len(array) == 1 {
		return array
	}
	if len(array) == 2 {
		if array[0] > array[1] {
			tmp := array[0]
			array[0] = array[1]
			array[1] = tmp
		}
		return array
	}

	left := array[:len(array)/2]
	leftSorted := mergeSort(left)

	right := array[len(array)/2:]
	rightSorted := mergeSort(right)

	sorted := []int{}
	n := len(leftSorted) + len(rightSorted)
	for i := 0; i < n; i++ {
		if leftSorted[0] > rightSorted[0] {
			sorted = append(sorted, rightSorted[0])
			rightSorted = rightSorted[1:]
			if len(rightSorted) == 0 {
				sorted = append(sorted, leftSorted...)
				return sorted
			}
		} else {
			sorted = append(sorted, leftSorted[0])
			leftSorted = leftSorted[1:]
			if len(leftSorted) == 0 {
				sorted = append(sorted, rightSorted...)
				return sorted
			}
		}
	}
	fmt.Println(sorted)
	return sorted
}
