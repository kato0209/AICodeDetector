package main
 
import "fmt"

func linearsearch(datalist []int, key int) bool {
	for _, item := range datalist {
		if item == key {
			return true
		}
	}
	return false
} 
 
func main() {
    items := []int{58,58,58,58,58,58,58,58,58,58}    fmt.Println(linearsearch(items,58))
}
