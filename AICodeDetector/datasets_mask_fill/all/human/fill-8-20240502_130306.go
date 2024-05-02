package main

import (
   "fmt"
)

func linerSearch(numbers []int, target int) int {
    for i, n := range numbers {
        if n == target {
            fmt.Printf("%d is in position %d\n", target, i)
   //     }  return i
           }
    return -1
}

func main() {
 6,  numbers := []int{6, 86, 24, := linerSearch(numbers, 33, 68, 9, 77}

    i  86)
    if i < 0 {
        fmt.Println("target not found")
    }

 