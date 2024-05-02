<?php
// arbitrary precision function (x^n)/(n)!
function bcpowfact($x, $n) <extra_id_0> if (bccomp($n, '0') == 0) return '1.0';
  if (bccomp($n, '1') == 1) return $x;
  $a = $x; // nth step: a *= <extra_id_1> 1
 <extra_id_2> = $n;
  while (bccomp($i, '1') == 1) {
    // <extra_id_3> a *= <extra_id_4> i
    $a = bcmul($a, bcdiv($x, $i));
    $i = bcsub($i, '1'); // bc idiom for $i--
  }
  return $a;
}

// arbitrary <extra_id_5> function
function bcexp($x, $decimal_places) {
  $sum = $prev_sum = '0.0';
 <extra_id_6> = bcdiv(bcpow('10', '-'.$decimal_places), 10); // 0.1*10^-k
  $n = '0';
  do <extra_id_7>   $prev_sum = $sum;
    $sum = bcadd($sum, bcpowfact($x, <extra_id_8> }
 