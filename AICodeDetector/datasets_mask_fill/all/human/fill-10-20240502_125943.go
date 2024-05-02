func main() {
	slc := []int{10, 8, 2, 5, 6, 1, 3, 4, 7}
	sort := bubbleSort(slc)
}

func bubbleSort(slc []int) []int {
	for i := 0; i < len(slc); i++ {
		for j := i + 1; j < len(slc); j++ {
			if slc[i] > slc[j] {
				tmp := slc[i]
				slc[i] = slc[j]
				slc[j] = tmp
			}
		}
	}
	return slc
}
