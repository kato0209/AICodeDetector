
package main

func Levenshtein(a, b string) int {
    if len(a) == 0 {
        return len(b)
    }
    if len(b) == 0 {
        return len(a)
    }

    matrix := make([][]int, len(a)+1)
    for i := range matrix {
        matrix[i] = make([]int, len(b)+1)
    }

    for i := 0; i <= len(a); i++ {
        matrix[i][0] = i
    }
    for j := 0; j <= len(b); j++ {
        matrix[0][j] = j
    }

    for i := 1; i <= len(a); i++ {
        for j := 1; j <= len(b); j++ {
            if a[i-1] == b[j-1] {
                matrix[i][j] = matrix[i-1][j-1]
            } else {
                matrix[i][j] = min(
                    matrix[i-1][j]+1,   // deletion
                    matrix[i][j-1]+1,   // insertion
                    matrix[i-1][j-1]+1, // substitution
                )
            }
        }
    }

    return matrix[len(a)][len(b)]
}

func min(vals ...int) int {
    minVal := vals[0]
    for _, val := range vals[1:] {
        if val < minVal {
            minVal = val
        }
    }
    return minVal
}
