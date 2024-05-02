<?php
function mergeSort($arr) {
    <extra_id_0> 1 ) return $arr;
    $mid = count($arr) / 2;
   <extra_id_1> = array_slice($arr, 0, $mid);
    $right = array_slice($arr, <extra_id_2>  <extra_id_3> = mergeSort($left);
    $right = <extra_id_4>   return merge($left, $right);
}

function merge($left, $right) {
    $res = array();
    while (count($left) > 0 && count($right) > 0) {
    <extra_id_5>   if($left[0] > $right[0]) {
          <extra_id_6> $res[] = $right[0];
    <extra_id_7>     <extra_id_8> $right = array_slice($right , 1);
        }else{
     