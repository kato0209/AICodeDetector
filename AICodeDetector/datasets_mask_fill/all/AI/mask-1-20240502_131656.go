
package main

func <extra_id_0> string) int {
    if len(a) == 0 {
  <extra_id_1>     return len(b)
    }
    if len(b) == 0 {
        return len(a)
    }

 <extra_id_2>  matrix := make([][]int, len(a)+1)
   <extra_id_3> i := range matrix <extra_id_4>     <extra_id_5> matrix[i] = make([]int, <extra_id_6>   <extra_id_7>   for i := 0; i <= len(a); i++ {
        matrix[i][0] = i
    }
   <extra_id_8> j := 0; j <= len(b); j++ {
        matrix[0][j] = j
