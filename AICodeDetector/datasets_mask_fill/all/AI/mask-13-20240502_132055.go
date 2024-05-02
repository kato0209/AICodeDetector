
package main

func Levenshtein(a, b string) int {
    alen, blen := len(a), len(b)
    if alen == 0 <extra_id_0>  <extra_id_1>    return blen
    }
    if blen == 0 {
  <extra_id_2>     return <extra_id_3>   }

 <extra_id_4>  matrix := make([][]int, alen+1)
    for i := range matrix {
     <extra_id_5>  matrix[i] = make([]int, blen+1)
        matrix[i][0] = i
    }
    for j := 1; j <= blen; j++ {
  <extra_id_6>     matrix[0][j] = <extra_id_7>   }

 <extra_id_8>  for