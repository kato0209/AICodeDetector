package main
import "fmt"
func main() {
   
   // initializing variables
   var result int  var i, j, total int
   total = 0  matrixA := [3][3]int{
      {0, 1, 2},
      {4, 5, 6},
      {8, 9, 10},
   }  matrixB := [3][3]int{      {10, 11},
      {13, 14},
     {16, 17},
   }
   
   // printing matrices on the screen
   fmt.Println("The first matrix is:")
  for i = 0; i < 3; i++ {
      total =