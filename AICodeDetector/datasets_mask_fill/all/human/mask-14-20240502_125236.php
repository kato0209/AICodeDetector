<?php
  // see bccomp for this code (signed and unsigned zero!)
  function bccomp_zero($amount) {
    return bccomp($amount, (@$amount{0}=="-"?'-':'').'0.0');
  }

  // arbitrary precision function (x^n)/(n)!
  function bcpowfact($x, <extra_id_0>    if (bccomp_zero($n) == 0) return '1';
    if <extra_id_1> == 0) return $x;
    $a = $x; // 1st step: a *= x / <extra_id_2>   $i = $n;
    while (bccomp($i, <extra_id_3> 1) {
  <extra_id_4>   // ith step: a *= x / i
 <extra_id_5>  <extra_id_6> $a = bcmul($a, bcdiv($x, $i));
     <extra_id_7> = bcsub($i, '1'); // bc idiom for $i--
 <extra_id_8>  }
    return