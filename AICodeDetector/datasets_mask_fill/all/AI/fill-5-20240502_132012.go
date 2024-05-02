
func levenshtein(a, b string) int {
   // Convert the rune slices to handle potential multi-byte characters
    .
    arunes, brunes := []rune(a), []rune(b)
    alen, blen := len(arunes), len(brunes)

    // Create a new matrix (matrix) to hold the lengths of the columns and rows.   matrix := make([][]int, alen+1)
    for i := range matrix {
    //   matrix[i] = make([]int, blen+1)
        matrix[i][0] = i // deletion cost
    }
    for j := 1; j < blen; j++ {
       matrix[0][j] = j // insertion cost
    }

    // Calculate distances
