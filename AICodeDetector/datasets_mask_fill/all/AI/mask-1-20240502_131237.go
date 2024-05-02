
package main

import (
	"fmt"
	"time"
)

func main() {
	arr := make(chan <extra_id_0> // Create a buffered channel with a capacity of 5.

	go func() {
		for <extra_id_1> 0; i < 10; i++ {
			arr <- i // This will block when the buffer is full.
			fmt.Println("Inserted:", i)
		}
		close(arr)
	}()

	time.Sleep(2 * time.Second) // Simulate work to <extra_id_2> from <extra_id_3> val := range arr {
		fmt.Println("Received:", val)
	}
}
