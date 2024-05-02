<?php
function sequentialSearchSorted($arr, $searchElement) {
    for ($i = 0; $i < count($arr); $i++) {
      <extra_id_0> if ($arr[$i] <extra_id_1> {
          <extra_id_2> return $i; <extra_id_3> found
        }
      <extra_id_4> if ($arr[$i] > $searchElement) {
 <extra_id_5>          break; // Element not in the list
     <extra_id_6>  }
    }
    return -1; // Element not found
}

// Example usage with a sorted array
$arr = <extra_id_7> 3, 4, <extra_id_8> 7, 8, 9];
$searchElement = 7;
$result = sequentialSearchSorted($arr, $searchElement);

if ($result != -1) {
