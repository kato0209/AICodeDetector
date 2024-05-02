<?php
// Function to simply sort on an array
function merge_sort($my_array){
    // Base case: if array has only one element, return it
    if(count($my_array) == 1) return $my_array;
    
    // Calculate the middle element of the array
    $mid = count($my_array) / 2;
    
    // Divide the array into two halves: left and right
    $left = array_slice($my_array, 0, $mid);
   $right = array_slice($my_array, $mid);
   
    // Recursively merge each side on each half
    $left = merge_sort($left);
    $right = merge_sort($right);
       // Merge the sorted halves
 