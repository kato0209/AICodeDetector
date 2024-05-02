package main

func binarySearch(arr []int, target int) int {
    left, <extra_id_0> 0, len(arr)-1
    <extra_id_1> <= right {
        mid := left + (right-left)/2
    <extra_id_2>   if arr[mid] == target {
            return mid
        }
 <extra_id_3>    <extra_id_4> if arr[mid] < target {
           <extra_id_5> = mid + 1
        } else <extra_id_6>         <extra_id_7> right = mid - 1
  <extra_id_8>  