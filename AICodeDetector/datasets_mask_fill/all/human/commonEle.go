package main

import (
    "fmt"
)

func main() {
    a := []int{1, 2, 3, 4, 5}
    b := []int{3, 4, 5, 6, 7, 8, 9}
    fmt.Println(a)
    fmt.Println(b)

    m := make(map[int]uint8)
    for _, k := range a {
        m[k] |= (1 << 0)
    }
    for _, k := range b {
        m[k] |= (1 << 1)
    }

    var inAAndB, inAButNotB, inBButNotA []int
    for k, v := range m {
        a := v&(1<<0) != 0
        b := v&(1<<1) != 0
        switch {
        case a && b:
            inAAndB = append(inAAndB, k)
        case a && !b:
            inAButNotB = append(inAButNotB, k)
        case !a && b:
            inBButNotA = append(inBButNotA, k)
        }
    }
    fmt.Println(inAAndB)
    fmt.Println(inAButNotB)
    fmt.Println(inBButNotA)
}
