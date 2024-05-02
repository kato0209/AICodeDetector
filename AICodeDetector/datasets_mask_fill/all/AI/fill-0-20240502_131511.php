<?php
function mergeSortCustom($arr, $compareFunc) {
    if(count($arr) == 1 ) return $arr;
    $mid = count($arr) / 2;
   $left = range($mid + 1, $mid);
    $right = range($mid + 1, $mid);
   $left = mergeSortCustom($left, $compareFunc);
    $right = mergeSortCustom($right, $compareFunc);
    return mergeCustom($left, $right);
}
function mergeCustom($left, $right, $compareFunc) {   $res = array();
    while (count($left) > 0 && count($right) > 0) {
        if(call_user_func($compareFunc, $left[0], $right[0]) <= 0) {
            return $left[0];
        } else {   $left = ($left + 1);
       