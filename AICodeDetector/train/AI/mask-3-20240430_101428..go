package main

import (
	"fmt"
)

// levenshteinIterative calculates the <extra_id_0> between two <extra_id_1> levenshteinIterative(str1, str2 string) int {
	lenStr1 := len(str1)
	lenStr2 := len(str2)
	dp := make([][]int, lenStr1+1)
	for i := range dp {
		dp[i] = make([]int, lenStr2+1)
	}

	for i := 0; i <extra_id_2> i++ {
		dp[i][0] = i
	}
	for j := 0; j <= lenStr2; j++ {
		dp[0][j] = j
	}

	for i := 1; <extra_id_3> lenStr1; i++ {
		for j := 1; j <= lenStr2; j++ <extra_id_4> 0
			if str1[i-1] != str2[j-1] {
				cost = 1
			}
			dp[i][j] <extra_id_5>   // Deletion
				min(
					dp[i][j-1]+1,       // <extra_id_6> Substitution
				),
			)
		}
	}
	return dp[lenStr1][lenStr2]
}

func min(a, b int) int <extra_id_7> < b {
		return a
	}
	return b
}

func main() {
	str1 := "kitten"
	str2 := "sitting"
	fmt.Printf("Levenshtein distance between '%s' and '%s' is %d\n", <extra_id_8> levenshteinIterative(str1, str2))
}
