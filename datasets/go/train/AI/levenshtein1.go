package main

import (
	"fmt"
)

// levenshteinIterative calculates the Levenshtein distance between two strings iteratively.
func levenshteinIterative(str1, str2 string) int {
	lenStr1 := len(str1)
	lenStr2 := len(str2)
	dp := make([][]int, lenStr1+1)
	for i := range dp {
		dp[i] = make([]int, lenStr2+1)
	}

	for i := 0; i <= lenStr1; i++ {
		dp[i][0] = i
	}
	for j := 0; j <= lenStr2; j++ {
		dp[0][j] = j
	}

	for i := 1; i <= lenStr1; i++ {
		for j := 1; j <= lenStr2; j++ {
			cost := 0
			if str1[i-1] != str2[j-1] {
				cost = 1
			}
			dp[i][j] = min(
				dp[i-1][j]+1,   // Deletion
				min(
					dp[i][j-1]+1,       // Insertion
					dp[i-1][j-1]+cost, // Substitution
				),
			)
		}
	}
	return dp[lenStr1][lenStr2]
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
	fmt.Printf("Levenshtein distance between '%s' and '%s' is %d\n", str1, str2, levenshteinIterative(str1, str2))
}
