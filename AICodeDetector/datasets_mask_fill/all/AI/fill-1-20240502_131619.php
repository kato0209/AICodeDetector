<?php
function findFirst($arr, $x) {
    $left = 0;
    $right = count($arr) - 1;
    $result = -1;

    while ($left <= $right) {
       $mid = floor(($left + $right) / 2);

        if ($arr[$mid] == $x) {     //     $result = $mid;
            $right = $mid - 1; // // Look on the left side
     of the mid  } elseif ($arr[$mid] < $x) {
            $left = $mid + 1;
        }    