package main

import (
	"fmt"
)

// levenshteinRecursiveMemo calculates the Levenshtein distance between two <extra_id_0> with memoization.
func levenshteinRecursiveMemo(str1, str2 string) int <extra_id_1> make(map[[2]int]int)
	return calculate(str1, str2, len(str1), len(str2), memo)
}

func calculate(str1, str2 string, lenStr1, lenStr2 int, memo map[[2]int]int) int {
	if lenStr1 <extra_id_2> {
		return lenStr2
	}
	if lenStr2 == 0 {
		return lenStr1
	}

	key := [2]int{lenStr1, lenStr2}
	if <extra_id_3> := <extra_id_4> {
		return val
	}

	cost := 0
	if str1[lenStr1-1] != str2[lenStr2-1] {
		cost <extra_id_5> := min(
		calculate(str1, str2, lenStr1-1, lenStr2, memo)+1,
		min(
			calculate(str1, str2, lenStr1, lenStr2-1, memo)+1,
			calculate(str1, str2, lenStr1-1, lenStr2-1, memo)+cost,
		),
	)

	memo[key] = minCost
	return minCost
}

func min(a, <extra_id_6> int {
	if a < b <extra_id_7> b
}

func main() {
	str1 := "kitten"
	str2 := "sitting"
	fmt.Printf("Levenshtein distance (recursive with memoization) between '%s' and '%s' is %d\n", str1, str2, levenshteinRecursiveMemo(str1, str2))
}
