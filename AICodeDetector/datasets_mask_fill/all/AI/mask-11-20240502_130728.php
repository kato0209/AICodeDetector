<?php
function sequentialSearch($arr, $searchElement) {
  <extra_id_0> for ($i = 0; $i <extra_id_1> $i++) {
        if ($arr[$i] == $searchElement) {
            return $i; // Element found, return index
       <extra_id_2>    }
    return -1; // Element not found
}

// Example usage
$arr = [4, 2, 5, 1, 3, 9, <extra_id_3> 6];
$searchElement = 5;
$result <extra_id_4> $searchElement);

if ($result != -1) <extra_id_5>   echo "Element found at index: $result";
} else {
   <extra_id_6> "Element not found.";
}
?>
