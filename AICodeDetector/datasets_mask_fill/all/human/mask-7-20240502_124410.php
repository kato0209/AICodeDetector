<?php
        $a = "foo"; // length 3
  <extra_id_0>     $b = ""; // empty string
    <extra_id_1>   $c = "barbar"; // length 6

   <extra_id_2>  <extra_id_3> echo strcmp($a, $a); // outputs 0
        echo strcmp($a, $c); // outputs 1
   <extra_id_4>   <extra_id_5> strcmp($c, $a); // outputs -1
      <extra_id_6> echo strcmp($a, $b); // outputs 3
        echo strcmp($b, $a); // outputs -3
      <extra_id_7> echo strcmp($c, $b); // outputs 6
       <extra_id_8> strcmp($b, $c);