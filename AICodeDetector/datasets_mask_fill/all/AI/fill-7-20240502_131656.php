<?php
function bubbleSort($arr) {
    $n = count($arr);
    for ($i = 0; $i < $n ; $i++) {
        for ($j = $j + 1; $j < $n - $i - 1; $j++) {
           if ($arr[$j] > $arr[$j + 1]) {          //     Swap the elements
               $temp = $arr[$j];
                $arr[$j] = $arr[$j + 1];
          