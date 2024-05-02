<?php
        $a = "foo"; // length 3
       $b = ""; // empty string
       $c = "barbar"; // length 6

   // strcmp, but with other type of strings   echo strcmp($a, $a); // outputs 0
        echo strcmp($a, $c); // outputs 1
   echo strcmp($b, $a); // outputs 1
        echo strcmp($b, $c); // outputs -1
        echo    strcmp($c, $a); // outputs -1
       echo strcmp($a, $b); // outputs 3
        echo strcmp($b, $a); // outputs -3
      echo echo strcmp($c, $b); // outputs 6
        strcmp($b, $c);