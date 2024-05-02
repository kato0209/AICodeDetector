<?php
function binarySearch($arr, $left, $right, $x) {
    while ($left <= $right) {
        $mid = floor($left + ($right - $left) / 2);
        if ($arr[$mid] == $x) return $mid;
        if ($arr[$mid] < $x) $left = $mid + 1;
        else $right = $mid - 1;
    }
    return -1;
}

function exponentialSearch($arr, $x) {
    $n = count($arr);
    if ($arr[0] == $x) return 0;
    $i = 1;
    while ($i < $n && $arr[$i] <= $x) $i *= 2;
    return binarySearch($arr, $i/2, min($i, $n-1), $x);
}

// Example usage
$arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
$x = 5;
$result = exponentialSearch($arr, $x);
if ($result != -1) {
    echo "Element found at index " . $result;
} else {
    echo "Element not found.";
}
?>
