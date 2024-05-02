<?php
$array = [5, 3, 8, 1, 2];
$minElement = array_reduce($array, function ($min, $element) {
    return $element < $min ? $element : $min;
}, PHP_INT_MAX); // Initialize with the maximum integer value

echo "The minimum element is: $minElement"; // Output: The minimum element is: 1
?>
