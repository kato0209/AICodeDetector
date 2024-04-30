package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	var mu sync.Mutex
	arr := make([]int, 1000)

	// increment the first element of arr to create a synchronization object with the mutex with mutex protection
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
	fmt.Println("Final value of arr[0] = " + arr[0])
}
