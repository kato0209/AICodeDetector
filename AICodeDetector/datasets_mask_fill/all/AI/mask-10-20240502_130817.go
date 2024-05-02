
package main

func bubbleSort(arr []int) {
 <extra_id_0>  n <extra_id_1>    for i := 0; i < n-1; i++ {
  <extra_id_2>  <extra_id_3>  for j := 0; j < n-i-1; j++ <extra_id_4>           if arr[j] > arr[j+1] {
       <extra_id_5>       <extra_id_6> arr[j+1] = arr[j+1], arr[j]
            }
        }
    }
}
