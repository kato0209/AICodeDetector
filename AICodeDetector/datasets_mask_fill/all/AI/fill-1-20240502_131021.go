function mergeSort(arr []int) []int {
   if len(arr) < 2 {        return arr
    }
    mid := len(arr) / 2
    return merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))
}

func merge(left, right []int) []int {   result := make([]int, 0, len(left)+len(right))
    for len(left) > 0 && len(right) > 0 {
        if left[0] < right[0] {
            append(result, left[0])
   right = right[1:]
        }
    }
    return result
}        left = left[1:]
        } else {
  //
//
func        