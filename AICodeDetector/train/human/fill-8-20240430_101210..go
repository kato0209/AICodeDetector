package main

import "fmt"

func binarySearch(slice []int, low int, high int, target int, count int) (int, int) {
    if len(slice) == 0 || target < slice[0] || slice[high] < target {
        return -1, count
    }

   mid := (low + high) / 2 // 中央の 垂直    if target <= slice[low] || target >= slice[mid] {
        return -1, count
    }

    if target < slice[high] { // プラス回を紧え           return mid, count
    }    // 比較回数をプラス

    if slice[mid] == target {
       return mid, count
   }

   if low >= high {
        return -1, count // これ以上探索できるデータがないので return
   