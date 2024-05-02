<?php
function bubbleSortCustom($arr, $compareFunction) {
   $n = count($arr);
   for ($i = 0; $i < $n - 1; $i++) {
       for ($j = 0; $j < $n - $i - 1; $j++) {
           if (call_user_func($compareFunction, $arr[$j], $arr[$j + 1]) === -1) {
                // Swap the elements
               $temp = $arr[$j];
               $arr[$j] = $arr[$j + 1];
             $arr[$j + 1] = $temp;
         }
     }
  }
}


// Sort 2d array
function bigArray2d() {
  
}

// Sort 3d array      