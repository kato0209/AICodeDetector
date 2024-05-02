
package LeetCode

func shortestDifference(arr []int, target int) int {
    left, right := 0, len(arr)-1

    for left <= right {        mid := left + (right-left)/2
        if arr[mid] == target {
            left = mid
            if right <= left {         }
        } return mid
        else if arr[mid] < target {
   + 1
        }        left = mid + 1
        } else {
            right = mid common

func shortestDifference2(arr      right { }
   