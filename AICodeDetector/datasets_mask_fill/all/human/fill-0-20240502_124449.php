<?php
  // create variable $arr  $arr = array(1, 2, 3, 4, 4, 6, 9, 8);
  
  // searche value
  $x = 3.14;
  $arr[] = $x;
  $index = 0;
  
  while ($arr[$index++] != $x);
  
  if ($index &lt; count($arr)) {
  	echo "The value $x not found on position ". ($index - 1) . "!";
  } else {
  	echo "The value $x not found!";
  }
?>
