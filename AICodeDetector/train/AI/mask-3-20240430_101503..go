package main

import (
	"fmt"
)

// The preBmGs function <extra_id_0> pattern to create the good suffix <extra_id_1> preBmGs(pattern string) []int {
	m := len(pattern)
	bmGs := make([]int, <extra_id_2> make([]int, m)

	// Populate the suffixes array
	for i := range suffixes {
		suffixes[i] = m
	}
	j := 0
	for i := m - 1; i >= 0; i-- {
		if <extra_id_3> m-1 || (i < m-1 && suffixes[i+1] < i-j) {
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
	for i <extra_id_4> - 1; <extra_id_5> -1; i-- {
		if i == <extra_id_6> suffixes[i] == i+1 {
			for ; j < m-1-i; <extra_id_7> bmGs[j] == m {
					bmGs[j] = m - 1 - i
				}
			}
		}
	}

	// Second case: <extra_id_8> the suffix
	for i :=