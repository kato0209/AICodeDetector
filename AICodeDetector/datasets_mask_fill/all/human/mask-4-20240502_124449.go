package main

import "fmt"

func minFind(arr []int) int {
  <extra_id_0> := arr[0]
   for _, num1 := range <extra_id_1>    <extra_id_2> if num1 <extra_id_3> {
         min = num1
      }
 <extra_id_4> }
   return min
}

func main() {
   arr := []int{20, 10, 45, 8, 12}
   min := minFind(arr)
   fmt.Printf("The minimum element <extra_id_5> array is: %d", min)
}
