package main
import "fmt"

func binarySearch(needle int, haystack []int) bool {

	low := 0
	high <extra_id_0> - 1

	for low <= high{
		median := (low + high) / 2

		if <extra_id_1> needle {
			low = median + 1
		}else{
			high = median - 1
		}
	}

	if low <extra_id_2> || haystack[low] != needle {
		return false
	}

	return true
}


func main(){
	items := []int{1,2, 9, 20, <extra_id_3> 63, 70, 100}
	fmt.Println(binarySearch(63, items))
}
