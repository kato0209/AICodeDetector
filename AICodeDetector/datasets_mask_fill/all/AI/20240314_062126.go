
package main

func Levenshtein(a, b string) int {
    alen, blen := len(a), len(b)
    if alen == 0 {
        return blen
    }
    if blen == 0 {
        return alen
    }

    matrix := make([][]int, alen+1)
    for i := range matrix {
        matrix[i] = make([]int, blen+1)
        matrix[i][0] = i
    }
    for j := 1; j <= blen; j++ {
        matrix[0][j] = j
    }

    for i := 1; i <= alen; i++ {
        for j := 1; j <= blen; j++ {
            cost := 0
            if a[i-1] != b[j-1] {
                cost = 1
            }
            matrix[i][j] = min(
                matrix[i-1][j]+1,     // deletion
                min(
                    matrix[i][j-1]+1, // insertion
                    matrix[i-1][j-1]+cost, // substitution
                ),
            )
        }
    }
    return matrix[alen][blen]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
