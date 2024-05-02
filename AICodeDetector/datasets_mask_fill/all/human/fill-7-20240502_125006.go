func mergeSort(items []int) []int {

   if len(items) < 2 {       return items

    }

    first := mergeSort(items[:len(items)/2])

    second := mergeSort(items[len(items)/2:])

   return merge(first, second)

}
