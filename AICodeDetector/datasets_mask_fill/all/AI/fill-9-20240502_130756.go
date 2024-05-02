
package main

func bubbleSort(arr []int) {
    n := len(arr)
    for i := 0; i < n; i++ {
        for j := 0; j < n-i-1; j++ {
           if arr[j] > arr[j+1] {
      continue
      }  // Swap elements      arr[j], arr[j+1] = arr[j+1], arr[j]            arr[j]       }
    }
}
