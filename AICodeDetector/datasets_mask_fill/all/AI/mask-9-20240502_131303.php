<?php
function sequentialSearch($arr, $searchElement) {
   <extra_id_0> ($i = 0; $i < count($arr); $i++) {
  <extra_id_1>    <extra_id_2> ($arr[$i] == <extra_id_3>            return $i; // Element found, return <extra_id_4>   <extra_id_5>   }
    }
    return -1; <extra_id_6> not found
}

// Example usage
$arr = [4, 2, 5, 1, 3, 9, 8, 11, 6];
$searchElement = 5;
$result = sequentialSearch($arr, $searchElement);

if ($result != -1) {
    echo "Element found at index: $result";
} else {
    echo "Element not found.";
}
?>
