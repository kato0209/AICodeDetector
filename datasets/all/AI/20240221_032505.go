package main

import (
    "fmt"
)

func binarySearch(arr []int, target int) int {
    start := 0
    end := len(arr) - 1

    for start <= end {
        mid := start + (end-start)/2

        if arr[mid] == target {
            return mid
        } else if arr[mid] < target {
            start = mid + 1
        } else {
            end = mid - 1
        }
    }

    return -1
}

func main() {
    arr := []int{1, 3, 5, 7, 9, 11, 13, 15}
    target := 7

    idx := binarySearch(arr, target)
    fmt.Println("Index of target:", idx)
}