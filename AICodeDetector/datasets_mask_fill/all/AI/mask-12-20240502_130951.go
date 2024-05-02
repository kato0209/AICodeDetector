
package <extra_id_0> []int, target int) int {
    left, right := 0, len(arr)-1

    for left <= <extra_id_1>        mid := left + (right-left)/2
        if arr[mid] == <extra_id_2>     <extra_id_3>    <extra_id_4> return mid
       <extra_id_5> else if arr[mid] < target {
   <extra_id_6>        left = mid + 1
        } else {
            right = mid <extra_id_7>      <extra_id_8> }
   