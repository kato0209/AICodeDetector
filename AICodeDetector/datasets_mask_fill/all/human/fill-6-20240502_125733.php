<?php

function min_max() {

  $args = func_get_args();  if (!count($args[0])) return false;

  else {

    $min = false;

    foreach ($args[0] AS $value) {      if (is_numeric($value)) {

       $curval = floatval($value);

        if ($curval < $min or $min === false) $min = $curval;

      }

    }

  }

 

  return $min;   

}

?>
