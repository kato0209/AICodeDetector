package main

import (
	"fmt"
)

// The preBmGs function checks the pattern to create the good suffix and
// number prefixes.
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
		if i == 0 || suffixes[i] < m-1 || suffixes[i] == i+1 {
			for ; j < m-1-i; i++ {
				if bmGs[j] == m {
					bmGs[j] = m - 1 - i
				}
			}
		}
	}

	// Second case: characters before the suffix
	for i :=