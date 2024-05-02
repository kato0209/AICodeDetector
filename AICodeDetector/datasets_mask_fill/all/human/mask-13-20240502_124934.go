package main
import <extra_id_0>  <extra_id_1> a function <extra_id_2> matrices
func MultiplyMatrix(matrixA [3][3]int, matrixB [3][2]int) [3][2]int {
   var total int = 0
   var result [3][2]int

   // multiplying matrices and storing result
   for i := 0; i < 3; i++ {
      <extra_id_3> := <extra_id_4> < 2; j++ {
       <extra_id_5> for k := 0; <extra_id_6> 3; k++ {
            total = total + matrixA[i][k]*matrixB[k][j]
       <extra_id_7> }
       <extra_id_8> result[i][j] = total
         total = 0
 