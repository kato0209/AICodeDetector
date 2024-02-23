package main

import(
    "fmt"
)

func binarySearch(arr []int, target int) int {
    lo := 0
    hi := len(arr) - 1
    
    for lo <= hi {
        mid := lo + (hi - lo) / 2
        
        if arr[mid] == target {
            return mid
        } else if arr[mid] < target {
            lo = mid + 1
        } else {
            hi = mid - 1
        }
    }
    
    return -1
}

func main() {
    arr := []int{2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    target := 14
    
    result := binarySearch(arr, target)
    fmt.Println("Index of", target, "in the array is:", result)
}
