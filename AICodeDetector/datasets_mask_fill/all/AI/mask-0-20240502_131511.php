<?php
function mergeSortCustom($arr, $compareFunc) {
    if(count($arr) == 1 ) return $arr;
    $mid = count($arr) / 2;
   <extra_id_0> = <extra_id_1> $mid);
    $right <extra_id_2> $mid);
  <extra_id_3> $left = mergeSortCustom($left, $compareFunc);
    $right = mergeSortCustom($right, $compareFunc);
    return mergeCustom($left, <extra_id_4> mergeCustom($left, $right, $compareFunc) <extra_id_5>   $res = array();
    while (count($left) > 0 && count($right) > 0) {
        if(call_user_func($compareFunc, $left[0], $right[0]) <= 0) {
            <extra_id_6> $left[0];
        <extra_id_7>   $left <extra_id_8> 1);
       