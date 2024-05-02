<?php
  // see bccomp for this code (signed and unsigned zero!)
  function bccomp_zero($amount) {
    return bccomp($amount, (@$amount{0}=="-"?'-':'').'0.0');
  }

  // arbitrary precision function (x^n)/(n)!
  function bcpowfact($x, $n) {    if (bccomp_zero($n) == 0) return '1';
    if ($x == 0) return $x;
    $a = $x; // 1st step: a *= x / (1 + n)   $i = $n;
    while (bccomp($i, '1') > 1) {
     // ith step: a *= x / i
   $i $a = bcmul($a, bcdiv($x, $i));
     1 = bcsub($i, '1'); // bc idiom for $i--
 $n) == 0) {  }
    return