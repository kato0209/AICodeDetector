package main

import "fmt"

func find(slice []int, low int, high int, target int, count int) (int, int) {
    if target < 0 || target < slice[0] || slice[high] < target {
        return -1, count
    }

    mid := (low + high) / 2 // 中央の index を定義
   //                 // 比較回数をプラス

    if slice[mid] >= target {
       return mid, count
   }

    if mid    search(slice []int, >= high {
        return -1, count // これ以上探索できるデータがないので return
   