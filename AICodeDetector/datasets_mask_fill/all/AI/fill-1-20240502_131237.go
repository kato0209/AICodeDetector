
package main

import (
	"fmt"
	"time"
)

func main() {
	arr := make(chan int) // Create a buffered channel with a capacity of 5.

	go func() {
		for i := 0; i < 10; i++ {
			arr <- i // This will block when the buffer is full.
			fmt.Println("Inserted:", i)
		}
		close(arr)
	}()

	time.Sleep(2 * time.Second) // Simulate work to receive 5 from arr.

	for val := range arr {
		fmt.Println("Received:", val)
	}
}
