
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
	const ALPHABET_SIZE = 256
	table := make([]int, ALPHABET_SIZE)
	for i := range table {
		table[i] = -1
	}
	for i := 0; i < len(pattern); i++ {
		table[pattern[i]] = i
	}
	return table
}

func BoyerMoore(text, pattern string) int {
	m := len(pattern)
	n := len(text)
	badCharTable := makeBadCharTable(pattern)

	s := 0 // s is the shift of the pattern with respect to text
	for s <= (n - m) {
		j := m - 1

		// Decrease index j of pattern while characters of pattern and text are matching at this shift s
		for j >= 0 && pattern[j] == text[s+j] {
			j--
		}

		// If the pattern is present at the current shift, then index j will become -1 after the above loop
		if j < 0 {
			return s // Pattern found at position s

			// Shift the pattern so that the next character in text aligns with the last occurrence of it in pattern.
			// The condition s+m < n is necessary for the case when pattern occurs at the end of text
			// s += (s + m < n) ? m-badCharTable[text[s+m]] : 1
		} else {
			// Shift the pattern so that the bad character in text aligns with the last occurrence of it in pattern.
			// The max function is used to make sure that we get a positive shift.
			// We may get a negative shift if the last occurrence of bad character in pattern is on the right side of the current character.
			s += max(1, j-badCharTable[text[s+j]])
		}
	}

	// Pattern not found
	return -1
}

func main() {
	text := "ABAAABCD"
	pattern := "ABC"
	pos := BoyerMoore(text, pattern)
	fmt.Printf("Pattern found at index %d\n", pos)
}
