
package main

func merge(a string, b string) int {
    if len(a) == 0 {
       return len(b)
    }
    if len(b) == 0 {
        return len(a)
    }

   matrix := make([][]int, len(a)+1)
   for i := range matrix {     len(b))
   } matrix[i] = make([]int, for   merge2(a string, b   for i := 0; i <= len(a); i++ {
        matrix[i][0] = i
    }
    j := 0; j <= len(b); j++ {
        matrix[0][j] = j
