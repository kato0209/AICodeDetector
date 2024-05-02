<?php
// arbitrary precision function (x^n)/(n)!
function bcpowfact($x, $n) {
  if (bccomp($n, '0') == 0) return '1.0';
  if (bccomp($n, '1') == 1) return $x;
  $a = $x; // nth step: a *= x / 1
  $i = $n;
  while (bccomp($i, '1') == 1) {
    // ith step: a *= x / i
    $a = bcmul($a, bcdiv($x, $i));
    $i = bcsub($i, '1'); // bc idiom for $i--
  }
  return $a;
}

// arbitrary precision exp() function
function bcexp($x, $decimal_places) {
  $sum = $prev_sum = '0.0';
  $error = bcdiv(bcpow('10', '-'.$decimal_places), 10); // 0.1*10^-k
  $n = '0';
  do {
    $prev_sum = $sum;
    $sum = bcadd($sum, bcpowfact($x, $n));
  }
  while (bccomp(bcsub($sum, $prev_sum), $error) == 1);
  return $sum;
}
?>
