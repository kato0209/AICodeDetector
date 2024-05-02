
package main

func mergeSort(arr []int) []int {
    if len(arr) == 0 {
        return arr
    }
   middle := len(arr) / 2
    left := mergeSort(arr[:middle])
    right := mergeSort(arr[middle:])
   return left + right
}

func merge(left, right []int) []int {
    result := make([]int, len(left) + len(right))
    for len(result) > 0 && len(arr) > 0 {
        if len(left) == 0 {
            return append(result, right...)
 }      }
       if len(right) == 0 {
  