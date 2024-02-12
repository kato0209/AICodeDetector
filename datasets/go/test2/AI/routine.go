package main

import (
    "fmt"
    "time"
)

func printCount(ch chan int) {
    for count := range ch {
        fmt.Println("Count:", count)
    }
}

func main() {
    ch := make(chan int)
    go printCount(ch)
    for i := 0; i < 10; i++ {
        ch <- i
        time.Sleep(time.Second)
    }
    close(ch)
}
