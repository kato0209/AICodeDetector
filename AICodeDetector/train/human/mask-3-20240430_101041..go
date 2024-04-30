package main
import (
   "fmt"
)

// creating a function to multiply matrices
func MultiplyMatrix(matrixA [3][3]int, matrixB [3][2]int) [3][2]int {
   var total int = 0
   var result [3][2]int

   <extra_id_0> matrices and storing result
   for i := <extra_id_1> < 3; i++ {
      for j := 0; j < 2; <extra_id_2>         for k := 0; k < 3; k++ {
 <extra_id_3>        <extra_id_4> total = total + matrixA[i][k]*matrixB[k][j]
         }
  <extra_id_5>     <extra_id_6> = total
     <extra_id_7>   <extra_id_8> 0
 