package main

import "fmt"

const CharSetSize = 256

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func preprocess(pattern string, size int) [CharSetSize]int {
	var badChar [CharSetSize]int

	// Initialize all occurrences as -1
	for i := 0; i < CharSetSize; i++ {
		badChar[i] = -1
	}

	// Fill the actual value of last occurrence of a character
	for i := 0; i < size; i++ {
		badChar[int(pattern[i])] = i
	}

	return badChar
}
