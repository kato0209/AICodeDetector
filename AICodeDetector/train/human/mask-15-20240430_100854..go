<extra_id_0> "fmt"

func linearSearch(list []int, target int) int {
	for i, num := range list {
		if num == target {
			return i
		}
	}
	return -1
}

func main() {
	searchList := []int{13, 25, <extra_id_1> 5, 24, 7, 5, <extra_id_2> := 78

	if index := linearSearch(searchList, target); index != <extra_id_3> %d found at index %d\n", target, index)
	} else {
		fmt.Printf("Element %d not found in the list\n", target)
	}
}
