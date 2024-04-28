package main

import "fmt"

func minFind(arr []int) int {
   min := arr[0]
   for _, num1 := range arr {
      if num1 < min {
         min = num1
      }
   }
   return min
}

func main() {
   arr := []int{20, 10, 45, 8, 12}
   min := minFind(arr)
   fmt.Printf("The minimum element in the array is: %d", min)
}
