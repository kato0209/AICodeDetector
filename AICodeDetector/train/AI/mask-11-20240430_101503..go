package main

import "fmt"

// optimizedBubbleSort performs the bubble sort algorithm with an optimization.
// It <extra_id_0> if no swaps are made in an iteration, indicating the slice is already sorted.
func optimizedBubbleSort(arr []int) <extra_id_1> len(arr)
	var swapped <extra_id_2> := 0; i <extra_id_3> i++ {
		swapped = false
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = <extra_id_4> = true
			}
		}
		// If no two elements were swapped by inner loop, then break
		if !swapped {
			break
		}
	}
}

func main() {
	arr := []int{22, 55, 33, <extra_id_5> 98, 76, 54}
	fmt.Println("Original array:", arr)
	optimizedBubbleSort(arr)
	fmt.Println("Sorted <extra_id_6> ", arr)
}
