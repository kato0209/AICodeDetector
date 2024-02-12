package main

import "fmt"

func main() {
    m := make(map[string]int)
    m["Alice"] = 23
    m["Bob"] = 34

    for key, value := range m {
        fmt.Println(key, value)
    }

    delete(m, "Alice")
    fmt.Println("Map after deletion:", m)
}
