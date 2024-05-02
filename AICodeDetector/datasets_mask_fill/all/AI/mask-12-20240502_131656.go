
package main

func binarySearch(arr []int, target int) int {
  <extra_id_0> left, right := 0, len(arr)-1

    <extra_id_1> <= right {
        <extra_id_2> left + (right-left)/2

 <extra_id_3>  <extra_id_4>   if arr[mid] == target {
       <extra_id_5>    return mid
        } else if arr[mid] < target {
    <extra_id_6>       <extra_id_7> mid + 1
        } else {
   <extra_id_8>        right = mid - 1
        }
   