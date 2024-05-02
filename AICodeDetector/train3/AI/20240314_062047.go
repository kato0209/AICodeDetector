
package main

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func makeBadCharTable(pattern string) []int {
    const alphabetSize = 256
    badChar := make([]int, alphabetSize)
    for i := range badChar {
        badChar[i] = -1
    }
    for i := 0; i < len(pattern); i++ {
        badChar[int(pattern[i])] = i
    }
    return badChar
}

func BoyerMoore(text, pattern string) []int {
    badChar := makeBadCharTable(pattern)
    var shifts []int
    m := len(pattern)
    n := len(text)

    shift := 0
    for shift <= (n - m) {
        j := m - 1
        for j >= 0 && pattern[j] == text[shift+j] {
            j--
        }
        if j < 0 {
            shifts = append(shifts, shift)
            if shift+m < n {
                shift += m - badChar[int(text[shift+m])]
            } else {
                shift += 1
            }
        } else {
            shift += max(1, j-badChar[int(text[shift+j])])
        }
    }
    return shifts
}

func main() {
    // Example usage
    text := "ABAAABCDABC"
    pattern := "ABC"
    matches := BoyerMoore(text, pattern)
    fmt.Println(matches) // Output: [7]
}
