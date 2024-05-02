package main

import (
	"fmt"
)

// gcdRecursive computes the greatest common divisor (GCD) of a and b using recursion.
func gcdRecursive(a, b int) int {
	if b == 0 {
		return a
	}
	return gcdRecursive(b, a%b)
}

func main() {
	var a, b int = 48, 18
	fmt.Printf("The GCD of %d and %d is %d\n", a, b, gcdRecursive(a, b))
}
