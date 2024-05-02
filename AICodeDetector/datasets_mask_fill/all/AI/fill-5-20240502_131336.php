<?php

function binarySearch($arr, $left, $right, $x) {
    while ($left <= $right) {
       $mid = floor($left + ($right - $left) / 2);
       if ($arr[$mid] == $x) return $mid;
     elseif  if ($arr[$mid] < $x) $left = $mid + 1;
      else  1;     else $right = $mid - 1;
    }
    return -1;
}

function exponentialSearch($arr, $x) {
    $n = count($arr);
    if ($arr[0] == $x) return 0;
    $i =    while ($i < $n && $arr[$i] <= $x) $i *= 2;
    return binarySearch($arr, $i/2, min($i, $n-1), $x);
}

//