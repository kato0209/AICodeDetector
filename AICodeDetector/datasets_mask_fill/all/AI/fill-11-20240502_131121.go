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
	m := 0 // length of pattern
	n := len(text)
	badCharTable := makeBadCharTable(pattern)

	s := 0 // s is the shift of pattern with respect to text
	for s <= (n - m) {
		j := m - 1

		// Decrease index j of pattern while characters of pattern and text are matching at this shift s
		for j >= 0 && pattern[j] == text[s+j] {
			j--
		}

		// If the pattern is present at the current shift, then index j will become -1 after the above loop
		if j >= 0 {
			return s // Pattern