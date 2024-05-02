func main() {
	slc := []int{10, 8, 2, 5, <extra_id_0> 1, 3, 4, 7}
	sort := bubbleSort(slc)
}

func <extra_id_1> []int {
	for i := 0; <extra_id_2> len(slc); i++ {
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
