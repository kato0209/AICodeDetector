<?php
function binarySearchRecursive($arr, $left, $right, $x) <extra_id_0>   if ($right >= $left) {
       <extra_id_1> = floor($left + <extra_id_2> $left) / 2);

        if ($arr[$mid] == $x) {
            <extra_id_3>      <extra_id_4> }

  <extra_id_5>     if ($arr[$mid] > $x) {
            return binarySearchRecursive($arr, $left, $mid - <extra_id_6>      <extra_id_7> }

        return binarySearchRecursive($arr, $mid + <extra_id_8> $x);
    }

    return -1; // Element not found
}

//