package main
import "fmt"

func binarySearch(needle int, haystack []int) bool {

	low := <extra_id_0> len(haystack) - 1

	for low <= high{
		median := (low + high) / 2

		if haystack[median] < needle <extra_id_1> median + 1
		}else{
			high = median - 1
		}
	}

	if low == len(haystack) || haystack[low] <extra_id_2> {
		return false
	}

	return true
}


func main(){
	items := []int{1,2, <extra_id_3> 31, 45, 63, 70, 100}
	fmt.Println(binarySearch(63, items))
}
