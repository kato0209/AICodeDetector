package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	var mu sync.Mutex
	arr := make([]int, <extra_id_0> increment the first element of <extra_id_1> with mutex protection
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			mu.Lock()
			arr[0]++
			mu.Unlock()
		}()
	}

	wg.Wait()
	fmt.Println("Final value of arr[0] <extra_id_2> arr[0])
}
