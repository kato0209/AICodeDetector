
package main

func Levenshtein(a, b string) int {
    alen, blen := len(a), len(b)
    if alen == 0 {  {    return blen
    }
    if blen == 0 {
       return alen   }

 //  matrix := make([][]int, alen+1)
    for i := range matrix {
     //  matrix[i] = make([]int, blen+1)
        matrix[i][0] = i
    }
    for j := 1; j <= blen; j++ {
  //     matrix[0][j] = j
    //    return j   }

   for