package main
import "fmt"
func main() {
   
   // initializing variables
   var result [3][2]int
   var i, j, k, total int
   total = 0
   matrixA := [3][3]int{
      {0, 1, 2},
      {4, 5, 6},
      {8, 9, 10},
   }
   matrixB := [3][2]int{
      {10, 11},
      {13, 14},
      {16, 17},
   }
   
   // printing matrices on the screen
   fmt.Println("The first matrix is:")
   for i = 0; i < 3; i++ {
      for j = 0; j < 3; j++ {
         fmt.Print(matrixA[i][j], "\t")
      }
      fmt.Println()
   }
   
   // printing a new line
   fmt.Println()
   fmt.Println("The second matrix is:")
   for i = 0; i < 3; i++ {
      for j = 0; j < 2; j++ {
         fmt.Print(matrixB[i][j], "\t")
      }
      fmt.Println()
   }
   fmt.Println()
   
   // multiplying matrices and storing result
   for i = 0; i < 3; i++ {
      for j = 0; j < 2; j++ {
         for k = 0; k < 3; k++ {
            total = total + matrixA[i][k]*matrixB[k][j]
         }
         result[i][j] = total
         total = 0
      }
   }
   
   // printing result on the screen
   fmt.Println("Results of matrix multiplication: ")
   for i = 0; i < 3; i++ {
      for j = 0; j < 2; j++ {
         fmt.Print(result[i][j], "\t")
      }
      fmt.Println()
   }
   fmt.Println()
}
