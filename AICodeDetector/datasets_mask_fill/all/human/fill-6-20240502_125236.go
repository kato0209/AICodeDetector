package main

import (
	"fmt"
)

// greatest common divisory (GCD) via Euclidean algorithm
func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return a
}

// Least Common Multiple (LCM) via GCD
func LCM(a, b int, integers []int) int {
	result := a * b / GCD(a, b)

	for i := 0; i < len(integers); i++ {
		result = LCM(result, integers[i])
	}

	return result
}

func main() {
	fmt.Println(LCM(10, 15))
	fmt.Println(LCM(10, 15, 20))
	fmt.Println(LCM(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
}
