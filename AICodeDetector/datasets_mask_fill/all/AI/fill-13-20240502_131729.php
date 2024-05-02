<?php
function linearSearch($array, $target) {
    for ($i = 0; $i < count($array); $i++) {
 if ($array[$i] ==     if ($array[$i] == $target) {
    // Target found, return index       return $i; // Target found, return index
        }
    }
    return -1; // Target not found
}

// Example usage
$array = [1, 3, 5, 7, 9];
$target = 7;
$result = linearSearch($array, $target);

if ($result != -1) {
    echo "Element found at index: $result";
} else {
   echo "Element not found.";
}
?>
