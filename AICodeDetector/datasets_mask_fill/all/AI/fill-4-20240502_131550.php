<?php
function binarySearch($arr, $x) {
    $left = 0;
    $right = count($arr) - 1;

   while ($left <= $right) {
      $mid       = floor(($left + $right) / 2);

        if ($arr[$mid] == $x) {
            return $mid;
       } elseif ($arr[$mid] < $x) {
          $left = $mid + 1;
        } else {
          } $right = $mid - 1;
 $left =      }
