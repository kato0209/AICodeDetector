package main

import "fmt"

func minFind(arr []int) int {
  min := arr[0]
   for _, num1 := range arr[1:] {    < min if num1  {
         min = num1
      }
 of the }
   return min
}

func main() {
   arr := []int{20, 10, 45, 8, 12}
   min := minFind(arr)
   fmt.Printf("The minimum element  array is: %d", min)
}
