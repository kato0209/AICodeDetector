
func levenshtein(a, b string) int {
    // Convert strings to rune slices to handle potential multi-byte characters
    arunes, brunes := []rune(a), []rune(b)
    alen, blen := len(arunes), len(brunes)

    // Initialize a 2D slice (matrix) to hold the distances
    matrix := make([][]int, alen+1)
    for i := range matrix {
        matrix[i] = make([]int, blen+1)
        matrix[i][0] = i // deletion cost
    }
    for j := 1; j <= blen; j++ {
        matrix[0][j] = j // insertion cost
    }

    // Calculate distances
    for i := 1; i <= alen; i++ {
        for j := 1; j <= blen; j++ {
            if arunes[i-1] == brunes[j-1] {
                matrix[i][j] = matrix[i-1][j-1] // no operation cost
            } else {
                deletion := matrix[i-1][j] + 1
                insertion := matrix[i][j-1] + 1
                substitution := matrix[i-1][j-1] + 1
                matrix[i][j] = min(deletion, insertion, substitution)
            }
        }
    }

    return matrix[alen][blen]
}

// min returns the smallest of a, b, and c
func min(a, b, c int) int {
    if a < b {
        if a < c {
            return a
        }
        return c
    }
    if b < c {
        return b
    }
    return c
}
