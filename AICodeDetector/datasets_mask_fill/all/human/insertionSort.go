func insertionSort(nums []int) []int {
	lenNums := len(nums)

	for i := 1; i < lenNums; i++ {
		temp := nums[i]
		j := i - 1
		for j >= 0 && nums[j] > temp {
			nums[j+1] = nums[j]
			j -= 1
		}
		nums[j+1] = temp
	}
	return nums
}
