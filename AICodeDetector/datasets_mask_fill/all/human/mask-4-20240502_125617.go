package main

import "fmt"

func <extra_id_0> low int, high int, target int, count int) (int, int) {
    <extra_id_1> < <extra_id_2> target < slice[0] || slice[high] < target {
        return -1, count
    }

    mid := (low + high) / <extra_id_3> 中央の index を定義
   <extra_id_4>                 // 比較回数をプラス

    if slice[mid] <extra_id_5> {
       <extra_id_6> mid, count
   <extra_id_7>    <extra_id_8> >= high {
        return -1, count // これ以上探索できるデータがないので return
   