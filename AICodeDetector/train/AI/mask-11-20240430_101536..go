package main

import <extra_id_0> builds the <extra_id_1> table.
// It maps each character in the pattern to its last <extra_id_2> the pattern.
func buildBadCharTable(pattern string) []int {
	const <extra_id_3> 256 // Assuming ASCII
	table := make([]int, alphabetSize)
	for i := range table {
		table[i] = -1 // Initialize table with -1
	}
	for i, ch <extra_id_4> pattern {
		table[ch] = i
	}
	return table
}

// BoyerMoore searches for occurrences of 'pattern' in 'text' using the bad character <extra_id_5> pattern <extra_id_6> {
	m, n := len(pattern), len(text)
	table := buildBadCharTable(pattern)
	occurrences := []int{}

	for s := 0; s <= n-m; {
		j := m - 1
		for j >= 0 <extra_id_7> == text[s+j] {
			j--
		}
		if j < 0 {
			occurrences = append(occurrences, s)
			s += (m - table[text[s+m-1]] - 1)
		} else <extra_id_8> max(1, j-table[text[s+j]])
		}
	}

	return occurrences
}

func max(a, b int) int {
	if a >