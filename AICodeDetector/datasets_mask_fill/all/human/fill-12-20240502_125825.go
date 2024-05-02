package main

import (
   "fmt"  "math"
)

func main() {
   x := 172  result := math.Exp(x)
   fmt.Printf("The base-e exponential of %f is %f", x, result)
}
