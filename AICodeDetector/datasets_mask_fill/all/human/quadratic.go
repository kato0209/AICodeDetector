package main
import (

   // fmt package provides the function to print anything
   "fmt"
 
   // math package is to use all the math-related predefined functions
   "math"
)
func main() {
   
   // declaring the variables to store the value
   
   // of the coefficients of quadratic equation
   var a, b, c float64
   
   // declaring a variable of float type to store discriminant
   
   // of the quadratic equation
   var d float64
   
   // initializing the coefficients variable with respective value
   a = 1
   b = 1
   c = 1
   fmt.Println("Finding the roots of the equation with the below coefficients within the function:")
   fmt.Println("a =", a)
   fmt.Println("b =", b)
   fmt.Println("c =", c)
   
   // finding the discriminant using the respective formulae
   d = b*b - 4*a*c
   if d > 0 {
      fmt.Println("Roots are real and different.")
      root1 := (-b + math.Sqrt(d)) / (2 * a)
      root2 := (-b - math.Sqrt(d)) / (2 * a)
      fmt.Println("The roots are:")
      fmt.Println("First Root", root1)
      fmt.Println("Second Root", root2)
   } else if d == 0 {
      fmt.Println("Roots are equal and same.")
      root1 := (-b + math.Sqrt(d)) / (2 * a)
      fmt.Println("The root is", root1)
   } else {
      fmt.Println("Roots are complex.")
      realPart := -b / (2 * a)
      imaginaryPart := math.Sqrt(math.Abs(d)) / (2 * a)
      fmt.Println("The roots are:")
      fmt.Println("First Root", realPart, "+", "i", imaginaryPart)
      fmt.Println("Second Root", realPart, "-", "i", imaginaryPart)
   }
}
