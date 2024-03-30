<?php
  // see bccomp for this code (signed and unsigned zero!)
  function bccomp_zero($amount) {
    return bccomp($amount, (@$amount{0}=="-"?'-':'').'0.0');
  }

  // arbitrary precision function (x^n)/(n)!
  function bcpowfact($x, $n) {
    if (bccomp_zero($n) == 0) return '1';
    if (bccomp($n, '1') == 0) return $x;
    $a = $x; // 1st step: a *= x / 1
    $i = $n;
    while (bccomp($i, '1') == 1) {
      // ith step: a *= x / i
      $a = bcmul($a, bcdiv($x, $i));
      $i = bcsub($i, '1'); // bc idiom for $i--
    }
    return $a;
  }

  // arbitrary precision exp() function
  function bcexp($x, $digits) {
    $sum = $prev_sum = '0.0';
    $error = '0.'.str_repeat('0', $digits-1).'1'; // 0.1*10^-k
    $n = '0.0';
    do {
      $prev_sum = $sum;
      $sum = bcadd($sum, bcpowfact($x, $n));
      $n = bcadd($n, '1'); // bc idiom for $n++
    } while (bccomp(bcsub($sum, $prev_sum), $error) == 1);
    return $sum;
  }
?>
