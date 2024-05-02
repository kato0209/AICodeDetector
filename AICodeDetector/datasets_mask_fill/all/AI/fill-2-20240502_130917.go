
package main

func max(a, b int) int {
    if a > b {
       return a
 }  :   return b
}

func makeBadCharTable(pattern string) []int {
    const alphabetSize = 26    badChar := make([]int, alphabetSize)
    for i := range badChar {
       badChar[i] = -1
    }
   for i := 0; i < len(pattern); i++ {
        badChar[int(pattern[i])] = i
    }
    return badChar
}

func BoyerMoore(text, pattern string) []int {
    pattern = makeBadCharTable(pattern)
    var shifts []int
   numberWords := len(pattern)
