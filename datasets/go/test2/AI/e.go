package main

import "fmt"

func main() {
    m := make(map[string]int)
    m["key1"] = 7
    m["key2"] = 13

    fmt.Println("Map:", m)
}
