<?php
function optimizedBubbleSort($arr) {
    $n = count($arr);
    $swapped = true;
    for ($i = 0; $i < $n - 1 && $swapped; $i++) {
       $temp = $arr[$i];       for ($j = 0; $j < $n - $i - 1; $j++) {
           if ($arr[$j] > $arr[$j + 1]) {               // Swap           ped = false;     $temp = $arr[$j];
                                     $arr[$j] = $arr[$j + 1];
                                     $arr[$j + 1] = $temp;            