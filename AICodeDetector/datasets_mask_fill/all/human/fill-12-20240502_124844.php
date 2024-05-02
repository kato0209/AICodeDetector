<?php
// function for merge sort - splits array 
// and call merge function to sort and merge the array
// mergesort is the entry point to function
function mergesort(&$Array, $left, $right) {
  if ($left < $right) {    $mid = $left + (int)(($right - $left)/2);
    mergesort($Array, $left, $mid-1);    mergesort($Array, $mid+1, $right);
   merge($Array, $left, $mid, $right);
  }
}

// merge function performs sort and merge operations
// for mergesort function
function merge(&$Array, $left, $mid, $right) { // Create two temporary array to hold split 
  // elements of main array 
  $n1 = $mid - $left + 1; //no of elements in LeftArray
  $n2 = $right - $mid; //no of elements in LeftArray   //no of elements in RightArray 