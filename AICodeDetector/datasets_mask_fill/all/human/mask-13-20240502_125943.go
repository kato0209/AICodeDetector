func insertionSort(nums []int) []int {
	lenNums := len(nums)

	for i := 1; i < lenNums; i++ <extra_id_0> nums[i]
		j := i - 1
		for j >= 0 && nums[j] > temp {
			nums[j+1] = <extra_id_1> 1
		}
		nums[j+1] = temp
	}
	return nums
}
