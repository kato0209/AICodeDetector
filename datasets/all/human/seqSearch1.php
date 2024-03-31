<?php
  // unordered list
  $arr = array(1, 2, 3, 3.14, 5, 4, 6, 9, 8);
  // searched value
  $x = 3.14;
  $index = null;
  for ($i = 0; $i < count($arr); $i++) {
    if ($arr[$i] == $x) {
        $index = $i;
    }
  }
  if (isset($index)) {
    return true;
  } else {
    return false;
  }
?>
