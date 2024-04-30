package <extra_id_0> gcdIterative computes the greatest common divisor (GCD) of a and b using the iterative method.
func gcdIterative(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	var a, b int = 48, <extra_id_1> of <extra_id_2> %d is %d\n", a, b, gcdIterative(a, b))
}
