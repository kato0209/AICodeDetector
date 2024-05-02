package main

import (
	"fmt"
)

// greatest <extra_id_0> (GCD) via Euclidean algorithm
func GCD(a, b int) int {
	for b != 0 {
		t := b
		b = a % b
		a = t
	}
	return <extra_id_1> Least Common Multiple (LCM) via GCD
func LCM(a, b int, <extra_id_2> int {
	result := a * b / GCD(a, b)

	for i := 0; i < len(integers); i++ <extra_id_3> LCM(result, integers[i])
	}

	return result
}

func main() {
	fmt.Println(LCM(10, 15))
	fmt.Println(LCM(10, 15, 20))
	fmt.Println(LCM(1, 2, 3, 4, <extra_id_4> 7, 8, 9, 10))
}
