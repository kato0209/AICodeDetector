package main

import (
	"fmt"
)

// The preBmGs function pre-processes the pattern to create the good suffix skip array.
func preBmGs(pattern string) []int {
	m := len(pattern)
	bmGs := make([]int, m)
	suffixes := make([]int, m)

	// Populate the suffixes array
	for i := range suffixes {
		suffixes[i] = m
	}
	j := 0
	for i := m - 1; i >= 0; i-- {
		if i == m-1 || (i < m-1 && suffixes[i+1] < i-j) {
			j = i
		}
		if i > 0 {
			suffixes[i-j] = i
		}
	}

	// First case: characters after the mismatch
	for i := range bmGs {
		bmGs[i] = m
	}
	j = 0
	for i := m - 1; i >= -1; i-- {
		if i == -1 || suffixes[i] == i+1 {
			for ; j < m-1-i; j++ {
				if bmGs[j] == m {
					bmGs[j] = m - 1 - i
				}
			}
		}
	}

	// Second case: characters inside the suffix
	for i := 0; i < m-1; i++ {
		bmGs[m-1-suffixes[i]] = m - 1 - i
	}

	return bmGs
}

// BoyerMooreGoodSuffix searches for occurrences of 'pattern' in 'text' using both the bad character rule and the good suffix rule.
func BoyerMooreGoodSuffix(text, pattern string) []int {
	m, n := len(pattern), len(text)
	badCharTable := buildBadCharTable(pattern)
	goodSuffixTable := preBmGs(pattern)
	occurrences := []int{}

	for s := 0; s <= n-m; {
		j := m - 1
		for j >= 0 && pattern[j] == text[s+j] {
			j--
		}
		if j < 0 {
			occurrences = append(occurrences, s)
			s += goodSuffixTable[0]
		} else {
			badCharShift := max(1, j-badCharTable[text[s+j]])
			goodSuffixShift := goodSuffixTable[j+1]
			s += max(badCharShift, goodSuffixShift)
		}
	}

	return occurrences
}

func main() {
	text := "HERE IS A SIMPLE EXAMPLE"
	pattern := "EXAMPLE"
	occurrences := BoyerMooreGoodSuffix(text, pattern)
	fmt.Println("Pattern found at positions:", occurrences)
}
