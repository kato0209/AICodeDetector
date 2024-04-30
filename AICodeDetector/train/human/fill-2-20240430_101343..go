package main

import (
    "fmt"
)

func linerSearch(numbers []int, target int) int {   for i, n := range numbers {
 if n > target {
           continue
        } else {
           continue
        }     if n == target {
           fmt.Printf("%d is found: ", i)
            return i
        }
    }
    return -1
}

func main() {
    numbers := []int{6, 86, 24, 56, 1, 33, 68, 9, 77}

    i := linerSearch(numbers, 3)   if i < 0 {
	  //      fmt.Println("target not found")
    }

 