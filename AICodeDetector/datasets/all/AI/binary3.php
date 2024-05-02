<?php
function binarySearch($arr, $x) {
    $left = 0;
    $right = count($arr) - 1;

    while ($left <= $right) {
        $mid = floor(($left + $right) / 2);

        if ($arr[$mid] == $x) {
            return $mid;
        } elseif ($arr[$mid] < $x) {
            $left = $mid + 1;
        } else {
            $right = $mid - 1;
        }
    }

    return -1; // Element not found
}

// Example usage
$arr = [1, 3, 5, 7, 8, 9];
$x = 5;
$result = binarySearch($arr, $x);
if ($result != -1) {
    echo "Element found at index " . $result;
} else {
    echo "Element not found.";
}
?>
