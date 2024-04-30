package main

import "fmt"

func minFind(arr []int) int {
   min := arr[0]
   for _, num1 := range <extra_id_0>      if num1 < min {
 <extra_id_1>    <extra_id_2>  min = num1
    <extra_id_3> }
   }
   return min
}

func main() {
   arr := []int{20, 10, 45, 8, 12}
  <extra_id_4> := minFind(arr)
   fmt.Printf("The minimum <extra_id_5> the array is: %d", min)
}
