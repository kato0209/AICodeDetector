<extra_id_0> mergeSort(arr []int) []int {
  <extra_id_1> if len(arr) < <extra_id_2>        return arr
    }
    mid := len(arr) / 2
    return merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))
}

func merge(left, right []int) []int <extra_id_3>   result := make([]int, 0, len(left)+len(right))
    for <extra_id_4> 0 && len(right) > 0 {
        if left[0] < right[0] {
 <extra_id_5>          <extra_id_6> append(result, left[0])
   <extra_id_7>        left = left[1:]
        } else {
  <extra_id_8>        