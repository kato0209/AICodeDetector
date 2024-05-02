package main

import "fmt"

func main() {
    s := []int{1, 2, 3}
    s = append(s, 4, 5, 6)
    fmt.Println("Slice:", s)

    for i, v := range s {
        fmt.Printf("Index: %d, Value: %d\n", i, v)
    }
}
