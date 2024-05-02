<?php
function binarySearch($arr, $x) {
    <extra_id_0> 0;
    $right = count($arr) - 1;

 <extra_id_1>  while ($left <= $right) <extra_id_2>      <extra_id_3> = floor(($left + $right) / 2);

        if ($arr[$mid] == $x) {
            return $mid;
      <extra_id_4> } elseif ($arr[$mid] < $x) {
      <extra_id_5>  <extra_id_6>  $left = $mid + 1;
        } else {
          <extra_id_7> $right = $mid - 1;
 <extra_id_8>      }
