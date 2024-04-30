package main

import "fmt"

func binarySearch(slice []int, low int, high int, target int, count int) <extra_id_0> {
    if len(slice) <extra_id_1> || target < slice[0] || slice[high] < target {
        return -1, count
    }

   <extra_id_2> := (low + high) / 2 // 中央の <extra_id_3>    <extra_id_4>           <extra_id_5>    // 比較回数をプラス

    if slice[mid] == target {
       <extra_id_6> mid, count
 <extra_id_7>  }

  <extra_id_8> if low >= high {
        return -1, count // これ以上探索できるデータがないので return
   