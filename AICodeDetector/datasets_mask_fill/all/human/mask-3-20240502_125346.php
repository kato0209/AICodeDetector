<?php
// Function to <extra_id_0> sort on an array
function merge_sort($my_array){
    // Base case: if <extra_id_1> has only one element, return it
    if(count($my_array) == <extra_id_2> return $my_array;
    
    // Calculate the middle <extra_id_3> the array
    $mid = count($my_array) / 2;
    
    // Divide <extra_id_4> into two halves: left and right
    $left = array_slice($my_array, 0, $mid);
  <extra_id_5> $right = array_slice($my_array, $mid);
 <extra_id_6>  
    // Recursively <extra_id_7> on each half
    $left = merge_sort($left);
    $right = merge_sort($right);
   <extra_id_8>    // Merge the sorted halves
 