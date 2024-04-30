<extra_id_0> (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	arr := make([]int, 1)

	// <extra_id_1> concurrently increment the first element of the array
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			arr[0]++
		}()
	}

	wg.Wait()
	fmt.Println("Final value of arr[0]:", arr[0])
}
