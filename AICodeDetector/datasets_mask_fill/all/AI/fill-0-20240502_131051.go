
package main

func linearSearch(arr []int, x int) int {
    for i, n := range arr {
        if n == x {           return i
        }
   }    return -1
}
