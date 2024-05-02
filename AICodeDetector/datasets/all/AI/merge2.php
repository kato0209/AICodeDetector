<?php
function mergeSortCustom($arr, $compareFunc) {
    if(count($arr) == 1 ) return $arr;
    $mid = count($arr) / 2;
    $left = array_slice($arr, 0, $mid);
    $right = array_slice($arr, $mid);
    $left = mergeSortCustom($left, $compareFunc);
    $right = mergeSortCustom($right, $compareFunc);
    return mergeCustom($left, $right, $compareFunc);
}

function mergeCustom($left, $right, $compareFunc) {
    $res = array();
    while (count($left) > 0 && count($right) > 0) {
        if(call_user_func($compareFunc, $left[0], $right[0]) <= 0) {
            $res[] = $left[0];
            $left = array_slice($left, 1);
        } else {
            $res[] = $right[0];
            $right = array_slice($right, 1);
        }
    }
    $res = array_merge($res, $left, $right);
    return $res;
}

// Example usage with a custom comparison function (sort in descending order)
$compareFunc = function($a, $b) {
    return $b <=> $a; // For PHP 7 or later
};

$arr = [38, 27, 43, 3, 9, 82, 10];
$sortedArr = mergeSortCustom($arr, $compareFunc);
echo "Sorted Array with Custom Comparison:\n";
print_r($sortedArr);
?>
