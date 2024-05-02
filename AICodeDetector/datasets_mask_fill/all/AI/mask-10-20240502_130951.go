
package main

func mergeSort(arr []int) []int {
    if len(arr) <extra_id_0> {
        return arr
    }
   <extra_id_1> := len(arr) / 2
    left := mergeSort(arr[:middle])
    right := mergeSort(arr[middle:])
  <extra_id_2> return <extra_id_3> merge(left, right []int) []int {
    result := make([]int, <extra_id_4> + len(right))
    for <extra_id_5> 0 <extra_id_6> > 0 {
        if len(left) == 0 {
            return append(result, right...)
 <extra_id_7>      }
   <extra_id_8>    if len(right) == 0 {
  