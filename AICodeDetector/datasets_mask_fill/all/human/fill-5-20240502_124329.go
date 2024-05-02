package main
import "fmt"

// 1. Go Program to get common elements 2. Golang Program to find the common elements from two arrays
func intersection(arr1, arr2 []string) []string {
   out := []string{}
   bucket := make(map[string]bool)  for _, i := range arr1 {
     for _, j := range arr2 {
        if i == j && bucket[j] == true {
            out = append(out, i)
            bucket[i] = true        }
     }
   }
  }     return out
}
func main() {
   arr1 := []string{"apple",