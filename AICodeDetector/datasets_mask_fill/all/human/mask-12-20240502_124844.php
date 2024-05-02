<?php
// function for merge sort - splits <extra_id_0> 
// and call merge function to sort and merge the array
// mergesort is <extra_id_1> function
function mergesort(&$Array, $left, $right) {
  if ($left < $right) <extra_id_2>    $mid = $left + (int)(($right - $left)/2);
    mergesort($Array, <extra_id_3>    mergesort($Array, $mid+1, $right);
  <extra_id_4> merge($Array, $left, $mid, $right);
  }
}

// merge function performs sort and merge operations
// for mergesort function
function merge(&$Array, $left, $mid, $right) <extra_id_5> // Create two temporary array to hold split 
  // elements of main array 
  $n1 <extra_id_6> - $left + 1; //no of elements in LeftArray
  $n2 = $right - $mid; <extra_id_7>   //no <extra_id_8> in RightArray 