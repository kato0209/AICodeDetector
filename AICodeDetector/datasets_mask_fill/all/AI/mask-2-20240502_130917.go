
package main

func max(a, b int) int {
    if a > b {
 <extra_id_0>      return a
 <extra_id_1>  <extra_id_2>   return b
}

func makeBadCharTable(pattern string) []int {
    const alphabetSize <extra_id_3>    badChar := make([]int, alphabetSize)
    for i := <extra_id_4> {
  <extra_id_5>     badChar[i] = -1
    }
 <extra_id_6>  for i := 0; i < len(pattern); i++ {
        badChar[int(pattern[i])] = i
    }
    return badChar
}

func BoyerMoore(text, pattern string) []int {
    <extra_id_7> makeBadCharTable(pattern)
    var shifts []int
   <extra_id_8> := len(pattern)
