<?php
function linearSearch($array, $target) {
    for ($i = <extra_id_0> < count($array); $i++) {
 <extra_id_1>   <extra_id_2>  if ($array[$i] == $target) {
    <extra_id_3>       return $i; // Target found, return index
        }
    }
    return -1; <extra_id_4> not found
}

// Example usage
$array = [1, 3, 5, 7, 9];
$target = 7;
$result <extra_id_5> $target);

if ($result != -1) {
    echo "Element found at index: $result";
} else {
  <extra_id_6> echo "Element not found.";
}
?>
