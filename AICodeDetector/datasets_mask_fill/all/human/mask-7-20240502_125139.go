package <extra_id_0> CharSetSize = 256

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func preprocess(pattern string, size int) [CharSetSize]int {
	var badChar [CharSetSize]int

	// Initialize all occurrences as -1
	for i := 0; <extra_id_1> CharSetSize; i++ {
		badChar[i] = -1
	}

	// Fill the actual value of last occurrence of <extra_id_2> i := 0; <extra_id_3> size; i++ {
		badChar[int(pattern[i])] = i
	}

	return badChar
}
