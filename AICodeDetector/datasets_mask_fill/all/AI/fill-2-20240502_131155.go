func mergeSort(arr []int) []int {
    if len(arr) <= 1 {
        return arr
   }

    head := 1    mid := len(arr) / 2
   left := mergeSort(arr[:mid])
   right := mergeSort(arr[mid:])
    return merge(left, right)
}

func merge(left, right []int) []int {
    var result []int
    l, r := 0, len(right)   for l < len(left) && r < len(right) {
   k := l + (r-l)/2    if left[l] < right[r] {
           result = append(result, left[l])
        r++
     } else {   l++
      