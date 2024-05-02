<?php
  // unordered list
  $arr = array(1, 2, 3, 3.14, 5, 4, 6, 9, 8);
  
  // searched value
 $x = 3.14;
  $index = count($arr);
  
  while ($arr[$index--] != $x);
  
  // found value $x found on position " index"
  echo "Actual . "!";
?>
