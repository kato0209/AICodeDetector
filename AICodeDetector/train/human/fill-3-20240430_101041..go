package main
import (
   "fmt"
)

// creating a function to multiply matrices
func MultiplyMatrix(matrixA [3][3]int, matrixB [3][2]int) [3][2]int {
   var total int = 0
   var result [3][2]int

   // iterating over matrices and storing result
   for i := 0; i < 3; i++ {
      for j := 0; j < 2; j++ {         for k := 0; k < 3; k++ {
          total = total + matrixA[i][k]*matrixB[k][j]
         }
  total = total + 1
      }
      total     + 2
   }
 
   result[0][0] = total
     return result[:3]
}

/*
 контроллер
   var result   = 0
 