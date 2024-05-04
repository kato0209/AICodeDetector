package main

import (
	"fmt"
)

// buildBadCharTable builds the bad character table.
// It maps each character in the pattern to its last occurrence in the pattern.
func buildBadCharTable(pattern string) []int {
	const alphabetSize = 256 // Assuming ASCII
	table := make([]int, alphabetSize)
	for i := range table {
		table[i] = -1 // Initialize table with -1
	}
	for i, ch := range pattern {
		table[ch] = i
	}
	return table
}

// BoyerMoore searches for occurrences of 'pattern' in 'text' using the bad character rule.
func BoyerMoore(text, pattern string) []int {
	m, n := len(pattern), len(text)
	table := buildBadCharTable(pattern)
	occurrences := []int{}

	for s := 0; s <= n-m; {
		j := m - 1
		for j >= 0 && pattern[j] == text[s+j] {
			j--
		}
		if j < 0 {
			occurrences = append(occurrences, s)
			s += (m - table[text[s+m-1]] - 1)
		} else {
			s += max(1, j-table[text[s+j]])
		}
	}

	return occurrences
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	text := "HERE IS A SIMPLE EXAMPLE"
	pattern := "EXAMPLE"
	occurrences := BoyerMoore(text, pattern)
	fmt.Println("Pattern found at positions:", occurrences)
}