
package main

import "fmt"

// ExponentialSearch searches for a target value within a sorted array using the exponential search algorithm.
// It returns the index of the target value if found; otherwise, it returns -1.
func ExponentialSearch(arr []int, target int) int {
    n := len(arr)
    if n == 0 {
        return -1
    }
    if arr[0] == target {
        return 0
    }
    i := 1
    for i < n && arr[i] <= target {
        i = i * 2
    }
    return binarySearch(arr, i/2, min(i, n-1), target)
}

// binarySearch is a helper function to perform binary search on the array.
// It is used once the range has been found by the exponential search.
func binarySearch(arr []int, left, right, target int) int {
    for left <= right {
        mid := left + (right-left)/2
        if arr[mid] == target {
            return mid
        }
        if arr[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return -1
}

// min is a helper function to find the minimum of two integers.
func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func main() {
    arr := []int{2, 3, 4, 10, 40, 50, 70, 100, 120}
    target := 40
    result := ExponentialSearch(arr, target)
    fmt.Printf("Element found at index: %d\n", result)
}
