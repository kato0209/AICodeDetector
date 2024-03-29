package main

import (
	"fmt"
)

// levenshteinRecursiveMemo calculates the Levenshtein distance between two strings recursively with memoization.
func levenshteinRecursiveMemo(str1, str2 string) int {
	memo := make(map[[2]int]int)
	return calculate(str1, str2, len(str1), len(str2), memo)
}

func calculate(str1, str2 string, lenStr1, lenStr2 int, memo map[[2]int]int) int {
	if lenStr1 == 0 {
		return lenStr2
	}
	if lenStr2 == 0 {
		return lenStr1
	}

	key := [2]int{lenStr1, lenStr2}
	if val, ok := memo[key]; ok {
		return val
	}

	cost := 0
	if str1[lenStr1-1] != str2[lenStr2-1] {
		cost = 1
	}

	minCost := min(
		calculate(str1, str2, lenStr1-1, lenStr2, memo)+1,
		min(
			calculate(str1, str2, lenStr1, lenStr2-1, memo)+1,
			calculate(str1, str2, lenStr1-1, lenStr2-1, memo)+cost,
		),
	)

	memo[key] = minCost
	return minCost
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	str1 := "kitten"
	str2 := "sitting"
	fmt.Printf("Levenshtein distance (recursive with memoization) between '%s' and '%s' is %d\n", str1, str2, levenshteinRecursiveMemo(str1, str2))
}
