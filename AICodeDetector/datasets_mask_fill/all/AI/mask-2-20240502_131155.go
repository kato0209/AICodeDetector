func mergeSort(arr []int) []int {
    if len(arr) <= 1 {
        return arr
   <extra_id_0>    mid := len(arr) / 2
  <extra_id_1> left := mergeSort(arr[:mid])
 <extra_id_2>  right := mergeSort(arr[mid:])
    return merge(left, right)
}

func merge(left, right []int) []int {
    var result []int
    l, r := 0, <extra_id_3>   for l < len(left) && r <extra_id_4> {
   <extra_id_5>    if left[l] <extra_id_6> {
          <extra_id_7> result = append(result, left[l])
        <extra_id_8>   l++
      