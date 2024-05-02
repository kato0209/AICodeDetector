func mergeSort(nums []int) []int {
	var lenNums = len(nums)

	if lenNums == <extra_id_0> nums
	}

	mid <extra_id_1> / 2
	var <extra_id_2> = make([]int, <extra_id_3> make([]int, lenNums-mid)
	)
	for i := 0; i < lenNums; i++ {
		if i < mid {
			left[i] = nums[i]
		} else {
			right[i-mid] = <extra_id_4> mergeSort(right))
}

func merge(left, right []int) (result []int) {
	result = make([]int, len(left)+len(right))

	i := 0
	for len(left) > 0 && len(right) > 0 {
		if left[0] < right[0] {
			result[i] = left[0]
			left = left[1:]
		} else {
			result[i] = right[0]
			right = right[1:]
		}
		i++
	}

	for j <extra_id_5> j < len(left); j++ {
		result[i] = left[j]
		i++
	}
	for j := 0; j < len(right); <extra_id_6> = right[j]
		i++
	}
	return
}
