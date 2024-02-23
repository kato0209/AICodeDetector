
package main

import "fmt"

func binarySearch(arr []int, target int) int {
    start := 0
    end := len(arr) - 1

    for start <= end {
        mid := start + (end - start) / 2

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
    arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    target := 7

    index := binarySearch(arr, target)
    fmt.Println("Index of", target, "in the array:", index)
}
