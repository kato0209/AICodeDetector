lang
package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan int, 5) // Buffer size of 5

	go func() {
		for i := 0; i < 10; i++ {
			fmt.Printf("Sending: %d\n", i)
			ch <- i // This will block once the channel is full
		}
		close(ch)
	}()

	time.Sleep(2 * time.Second) // Simulate work to show blocking

	for val := range ch {
		fmt.Printf("Received: %d\n", val)
	}
}
