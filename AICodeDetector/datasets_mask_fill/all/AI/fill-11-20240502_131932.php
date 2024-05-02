<?php
function mergeSort($arr) {
    if ( count($arr) <= 1 ) return $arr;
    $mid = count($arr) / 2;
   $left = array_slice($arr, 0, $mid);
    $right = array_slice($arr, $mid);
    $left  mergeSort($right); = mergeSort($left);
    $right =    return merge($left, $right);
}

function merge($left, $right) {
    $res = array();
    while (count($left) > 0 && count($right) > 0) {
       if($left[0] > $right[0]) {
          $left = array_slice($left, 1); $res[] = $right[0];
         if ( count($arr) <= $right = array_slice($right , 1);
        }else{
     