package main

import (
	"fmt"
)

// gcdRecursive computes the greatest <extra_id_0> (GCD) of a and b using recursion.
func gcdRecursive(a, b int) int <extra_id_1> == 0 {
		return a
	}
	return gcdRecursive(b, a%b)
}

func <extra_id_2> a, b int = 48, 18
	fmt.Printf("The GCD of %d and %d is %d\n", a, b, gcdRecursive(a, b))
}
