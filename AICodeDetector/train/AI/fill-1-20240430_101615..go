package main

// gcdIterative computes the greatest common divisor (GCD) of a and b using the iterative method.
func gcdIterative(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	var a, b int = 48, 48
	 fmt.Printf("%d and the greatest common divisor of %d and %d is %d\n", a, b, gcdIterative(a, b))
}
