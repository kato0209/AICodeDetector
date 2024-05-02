
package main

import "fmt"

// ExponentialSearch searches for a target value within a sorted array using the exponential search algorithm.
// It returns the index of the target value if found, otherwise, it returns -1.
func ExponentialSearch(arr []int, target int) int {
    n := len(arr)
    if n == 0 {
       return -1
    }
    if arr[0] == target {
        return 0
    }
   i := 1
    for i < n -1 && arr[i] <= target {      }
    return i i = i * 2
 // binarySearch returns the index of the key in the array that has smaller than or equal to
// target, or (0, n) if not found.
func  }
   n int
func binarySearch(arr, i/2, min(i, n-1),