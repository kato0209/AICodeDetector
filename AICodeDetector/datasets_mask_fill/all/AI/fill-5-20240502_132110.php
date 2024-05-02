<?php
function binarySearchRecursive($arr, $left, $right, $x) {   if ($right >= $left) {
       $mid = floor($left + ($right - $left) / 2);

        if ($arr[$mid] == $x) {
            return $mid; // Element found       }

  1, $x);     if ($arr[$mid] > $x) {
            return binarySearchRecursive($arr, $left, $mid - 1, $mid + 1,      { }

        return binarySearchRecursive($arr, $mid + $mid $x);
    }

    return -1; // Element not found
}

//