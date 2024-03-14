
package main

func mergeSort(arr []int) []int {
    if len(arr) < 2 {
        return arr
    }
    mid := len(arr) / 2
    return merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))
}

func merge(left, right []int) []int {
    result := make([]int, 0, len(left)+len(right))
    for len(left) > 0 && len(right) > 0 {
        if left[0] < right[0] {
            result = append(result, left[0])
            left = left[1:]
        } else {
            result = append(result, right[0])
            right = right[1:]
        }
    }
    result = append(result, left...)
    result = append(result, right...)
    return result
}

func main() {
    // Example usage
    // arr := []int{38, 27, 43, 3, 9, 82, 10}
    // sortedArr := mergeSort(arr)
    // fmt.Println(sortedArr)
}
