func mergeSort(items []int) []int {

  <extra_id_0> if len(items) < 2 <extra_id_1>       return items

    }

    first := mergeSort(items[:len(items)/2])

    second := mergeSort(items[len(items)/2:])

   <extra_id_2> merge(first, second)

}
