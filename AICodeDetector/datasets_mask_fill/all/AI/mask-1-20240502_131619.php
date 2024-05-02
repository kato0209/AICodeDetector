<?php
function findFirst($arr, $x) {
    $left = 0;
    $right = count($arr) - 1;
    $result = -1;

    while ($left <= $right) {
  <extra_id_0>     $mid = floor(($left + <extra_id_1> 2);

        <extra_id_2> == $x) <extra_id_3>     <extra_id_4>     $result = $mid;
            $right = $mid <extra_id_5> // Look on the left side
     <extra_id_6>  } elseif ($arr[$mid] < $x) {
            $left <extra_id_7> + <extra_id_8>    