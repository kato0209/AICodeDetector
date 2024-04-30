package main
import "fmt"

// function to get common elements 2. Golang Program to find the common <extra_id_0> two arrays
func intersection(arr1, arr2 []string) []string {
 <extra_id_1> out := []string{}
   bucket := map[string]bool{}
   for _, <extra_id_2> range arr1 <extra_id_3>     for <extra_id_4> := range arr2 {
       <extra_id_5> if i == j && !bucket[i] {
            out = <extra_id_6>            bucket[i] <extra_id_7>         }
   <extra_id_8>  }
   }
   return out
}
func main() {
   arr1 := []string{"apple",