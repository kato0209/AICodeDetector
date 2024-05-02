
package main

import (
	"fmt"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func makeBadCharTable(pattern string) []int {
	const alphabetSize = 256
	table := make([]int, alphabetSize)
	for i := range table {
		table[i] = -1
	}
	for i := 0; i < len(pattern); i++ {
		table[pattern[i]] = i
	}
	return table
}

func BoyerMoore(text, pattern string) []int {
	m := len(pattern)
	n := len(text)
	if m == 0 || n == 0 || m > n {
		return nil
	}
	badCharTable := makeBadCharTable(pattern)
	var res []int

	s := 0
	for s <= (n - m) {
		j := m - 1
		for j >= 0 && pattern[j] == text[s+j] {
			j--
		}
		if j < 0 {
			res = append(res, s)
			s += (m - badCharTable[text[s+m]])
		} else {
			s += max(1, j-badCharTable[text[s+j]])
		}
	}

	return res
}

func main() {
	text := "ABAAABCDABC"
	pattern := "ABC"
	matches := BoyerMoore(text, pattern)
	fmt.Println(matches) // Output: [7]
}
