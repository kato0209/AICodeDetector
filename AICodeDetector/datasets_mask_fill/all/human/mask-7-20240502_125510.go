package main

import (
   "fmt"
 <extra_id_0> "math"
)

func main() {
   x := 2.5
 <extra_id_1> result := math.Exp(x)
   fmt.Printf("The base-e exponential of %f is %f", x, result)
}
