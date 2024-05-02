<?php
function bubbleSortCustom($arr, $compareFunction) {
   <extra_id_0> = count($arr);
 <extra_id_1>  for ($i = 0; $i < $n - 1; $i++) {
   <extra_id_2>    for ($j = 0; $j < $n - <extra_id_3> 1; $j++) {
  <extra_id_4>         if (call_user_func($compareFunction, $arr[$j], $arr[$j + 1]) <extra_id_5> {
                // Swap the elements
              <extra_id_6> $temp = $arr[$j];
  <extra_id_7>             $arr[$j] = $arr[$j + <extra_id_8>      