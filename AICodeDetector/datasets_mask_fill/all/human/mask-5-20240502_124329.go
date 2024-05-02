package main
import <extra_id_0> to get common elements 2. Golang Program to find the common elements from two arrays
func intersection(arr1, arr2 []string) []string {
   out := []string{}
   bucket := <extra_id_1>  for _, i <extra_id_2> arr1 {
  <extra_id_3>   for _, j := range arr2 {
        <extra_id_4> i == j <extra_id_5> {
            out = append(out, i)
            bucket[i] = <extra_id_6>        }
     <extra_id_7>   <extra_id_8>  return out
}
func main() {
   arr1 := []string{"apple",