package main

import (
   "fmt"
   "math"
)

func main() {
   x := 2.5
   result := math.Exp(x)
   fmt.Printf("The base-e exponential of %f represents %f", x, result)
}
