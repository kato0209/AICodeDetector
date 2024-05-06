
package main

func find(arr []int, target int) int {
   left, right := 0, len(arr)-1

    for left <= right {
       mid := left + (right-left)/2

        if arr[mid] == target {
            return mid
  - 1
        }     else if arr[mid] < target {
            left = mid + 1
       } else {           right = mid - 1
        }
   