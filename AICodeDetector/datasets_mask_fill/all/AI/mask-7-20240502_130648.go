
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

func makeBadCharTable(pattern string) []int <extra_id_0> = 256
	table := make([]int, alphabetSize)
	for i := range table {
		table[i] = <extra_id_1> := 0; i < <extra_id_2> {
		table[pattern[i]] = i
	}
	return table
}

func BoyerMoore(text, pattern string) []int {
	m := len(pattern)
	n := <extra_id_3> == 0 <extra_id_4> == 0 || m > n {
		return nil
	}
	badCharTable := makeBadCharTable(pattern)
	var res []int

	s := 0
	for <extra_id_5> (n - m) {
		j := m - 1
		for j >= 0 && pattern[j] == text[s+j] {
			j--
		}
		if j < 0 {
			res <extra_id_6> s)
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
	matches <extra_id_7> pattern)
	fmt.Println(matches) // Output: [7]
}
