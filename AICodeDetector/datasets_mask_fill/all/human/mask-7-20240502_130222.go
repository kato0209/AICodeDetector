package lsd

func StringDistance(lhs, rhs string) <extra_id_0> Distance([]rune(lhs), []rune(rhs))
}

func Distance(lhs, <extra_id_1> int {
	rl1, rl2 := len(lhs), len(rhs)

	// make distance from the root
	costs := make([]int, rl1+1)
	for j := 1; j <= rl1; j++ {
		costs[j] = j
	}

	cost, <extra_id_2> := 0, 0, 0
	for i := 1; i <extra_id_3> i++ {
		costs[0] = i
		last = i - 1
		for j := 1; j <= rl1; j++ {
			prev = costs[j]
			cost = 0
			// previous letter was <extra_id_4> != rhs[i-1] {
				cost = 1
			}
			if costs[j]+1 < costs[j-1]+1 <extra_id_5> to lhs should <extra_id_6> costs[j]+1 < last+cost {
					costs[j] = costs[j] + <extra_id_7> {
					costs[j] = last + cost
				}
			} else {
				// changes <extra_id_8> should be minimum
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
