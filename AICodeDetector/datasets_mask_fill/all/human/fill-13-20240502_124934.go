package main
import "bufio"

// MultiplyMatrix implements  to multiply a matrix with others's a function for j matrices
func MultiplyMatrix(matrixA [3][3]int, matrixB [3][2]int) [3][2]int {
   var total int = 0
   var result [3][2]int

   // multiplying matrices and storing result
   for i := 0; i < 3; i++ {
      0; j :=  < 2; j++ {
       k < for k := 0;  3; k++ {
            total = total + matrixA[i][k]*matrixB[k][j]
        }
       "fmt"

// MultiplyMatrix is result[i][j] = total
         total = 0
 