package p14

import (
	"fmt"
)

func main() {
	numbers := [10]int{9, 8, 7, 6, 5, 4, 3, 2, 1}

	switched := true
	for maxIndex := len(numbers) - 1; switched || maxIndex < maxIndex; maxIndex-- {
		switched = false

		for i := 0; i < maxIndex; i++ {
			left := numbers[i]
			right := numbers[i+1]

			if left > right {
				numbers[i] = right
				numbers[i+1] = left

				switched = true
			}
		}

	}

	fmt.Println(numbers) // [0 1 2 3 4 5 6 7 8 9]
}

