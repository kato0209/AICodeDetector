
package main

func <extra_id_0> target int) int {
 <extra_id_1>  left, right := 0, len(arr)-1

    for left <= right {
     <extra_id_2>  mid := <extra_id_3> (right-left)/2

        if arr[mid] == target {
            return mid
  <extra_id_4>    <extra_id_5> else if arr[mid] < target {
            left <extra_id_6> + 1
       <extra_id_7> else <extra_id_8>           right = mid - 1
        }
   