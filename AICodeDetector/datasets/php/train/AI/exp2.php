<?php
// Assuming binarySearch() is defined as in Snippet 1

function exponentialSearchWithEarlyExit($arr, $x) {
    $n = count($arr);
    if ($arr[0] == $x) return 0;
    $i = 1;
    while ($i < $n && $arr[$i] < $x) {
        if ($arr[$i] == $x) return $i;
        $i *= 2;
    }
    // Perform binary search only on the identified range
    return binarySearch($arr, $i/2, min($i, $n-1), $x);
}

// Example usage remains the same as Snippet 1
?>
