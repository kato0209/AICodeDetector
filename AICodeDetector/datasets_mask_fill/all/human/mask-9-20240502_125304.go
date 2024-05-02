package <extra_id_0> main() {
	numbers := [10]int{9, 8, 7, 6, 5, 4, 3, 2, <extra_id_1> := true
	for maxIndex := len(numbers) - 1; switched <extra_id_2> < maxIndex; maxIndex-- {
		switched = false

		for i := 0; i < maxIndex; i++ {
			left := numbers[i]
			right := numbers[i+1]

			if left > <extra_id_3> = right
				numbers[i+1] = left

				switched = true
			}
		}

	}

	fmt.Println(numbers) // [0 1 2 3 4 5 6 7 8 9]
}

