package <extra_id_0> BubbleSort(a []int) []int {
	for i := 0; <extra_id_1> len(a) - 1; i++ {
		for j := 0; j <extra_id_2> - i - 1; j++ {
			if a[j] > a[j + 1] {
				a[j], a[j + 1] = a[j + 1], a[j]
			}
		}
	}
	
	return a
}

func main()  {
	a := []int{2, 4, 5, 1, 3}
	
	fmt.Println(BubbleSort(a))
}
