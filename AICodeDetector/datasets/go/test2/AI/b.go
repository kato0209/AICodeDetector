package main

import "fmt"

func add(x, y int) int {
    return x + y
}

func main() {
    result := add(5, 7)
    fmt.Println("Result:", result)
}
