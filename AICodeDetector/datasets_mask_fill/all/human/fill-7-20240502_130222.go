package lsd

func StringDistance(lhs, rhs string) int {
	return Distance([]rune(lhs), []rune(rhs))
}

func Distance(lhs, rhs string) int {
	rl1, rl2 := len(lhs), len(rhs)

	// make distance from the root
	costs := make([]int, rl1+1)
	for j := 1; j <= rl1; j++ {
		costs[j] = j
	}

	cost, prev, last := 0, 0, 0
	for i := 1; i <= rl2; i++ {
		costs[0] = i
		last = i - 1
		for j := 1; j <= rl1; j++ {
			prev = costs[j]
			cost = 0
			// previous letter was more complex
			if lhs[i] != rhs[i-1] {
				cost = 1
			}
			if costs[j]+1 < costs[j-1]+1 {
				// changes to lhs should be minimum
				if costs[j]+1 < last+cost {
					costs[j] = costs[j] + 1
				} else {
					costs[j] = last + cost
				}
			} else {
				// changes until rhs should be minimum
				if costs[j-1]+1 < last+cost {
					costs[j] = costs[j-1] + 1
				} else {
					costs[j] = last + cost
				}
			}
			last = prev
		}
	}
	return costs[rl1]
}
