<?php
function binarySearchRecursive($arr, $left, $right, $x) {
    if ($right >= $left) {
        $mid = floor($left + ($right - $left) / 2);

        if ($arr[$mid] == $x) {
            return $mid;
        }

        if ($arr[$mid] > $x) {
            return binarySearchRecursive($arr, $left, $mid - 1, $x);
        }

        return binarySearchRecursive($arr, $mid + 1, $right, $x);
    }

    return -1; // Element not found
}

// Example usage
$arr = [1, 3, 5, 7, 8, 9];
$x = 7;
$result = binarySearchRecursive($arr, 0, count($arr) - 1, $x);
if ($result != -1) {
    echo "Element found at index " . $result;
} else {
    echo "Element not found.";
}
?>
