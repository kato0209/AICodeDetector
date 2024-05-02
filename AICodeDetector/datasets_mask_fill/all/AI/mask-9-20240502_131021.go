<extra_id_0> (
	"fmt"
)

func commonElements(arr1, arr2 <extra_id_1> {
	common := []int{}
	m := make(map[int]bool)

	for _, value := range arr1 {
		m[value] = true
	}

	for _, value := range arr2 {
		if _, found := m[value]; found {
			common = append(common, value)
			delete(m, value) // <extra_id_2> elements
		}
	}
	return common
}

func main() {
	arr1 := []int{1, 2, 3, 4, 5}
	arr2 := []int{0, 2, 4, 6, 8}
	common <extra_id_3> arr2)
	fmt.Println(common)
}
