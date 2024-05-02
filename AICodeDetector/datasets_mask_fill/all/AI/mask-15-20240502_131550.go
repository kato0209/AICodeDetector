<extra_id_0> (
	"fmt"
)

// BinarySearch performs a binary search on a sorted slice.
func <extra_id_1> left int, right int, x <extra_id_2> {
	if right >= left {
		mid := left + (right-left)/2

		if arr[mid] == x {
			return mid
		}
		if arr[mid] > x {
			return BinarySearch(arr, left, <extra_id_3> BinarySearch(arr, mid+1, right, x)
	}
	return -1
}

// ExponentialSearch searches for a value in a sorted slice using exponential search.
func ExponentialSearch(arr <extra_id_4> int, x int) int {
	if arr[0] == x {
		return 0
	}

	i := 1
	for i < n && arr[i] <= x {
		i = i * 2
	}

	return BinarySearch(arr, i/2, <extra_id_5> x)
}

func min(x, y int) int {
	if <extra_id_6> y {
		return x
	}
	return y
}

func main() {
	arr := []int{2, 3, 4, 10, <extra_id_7> 10
	result := ExponentialSearch(arr, len(arr), x)
	if result != -1 {
		fmt.Printf("Element is <extra_id_8> index %d", result)
	} else