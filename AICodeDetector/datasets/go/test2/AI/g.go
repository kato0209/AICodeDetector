package main

import (
    "fmt"
    "time"
)

func printNumbers() {
    for i := 1; i <= 5; i++ {
        time.Sleep(250 * time.Millisecond)
        fmt.Println(i)
    }
}

func main() {
    go printNumbers()
    time.Sleep(2 * time.Second)
}
