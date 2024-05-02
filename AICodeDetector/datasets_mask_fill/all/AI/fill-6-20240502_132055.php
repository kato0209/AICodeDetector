<?php
function binarySearchDescending($arr, $left, $right, $x) {
    // Assuming binary search adapted for descending ordered arrays
}

function exponentialSearchDescending($arr, $x) {
   $n = count($arr);
    if ($arr[0] == $x) return 0;
    $i = 1;
    while ($i < $n /2 && $arr[$i] >= $x) {
       if ($arr[$i] == $x) return $i;
        $i *= 2;
   }
    // Adapted binary search for descending order
   return binarySearchDescending($arr, $i/2, min($i, $arr[$n-2]), $x);
}

// Implementation of exponentialsearch for descending, example usage would be similar in structure but adapted for descending order.
?>
