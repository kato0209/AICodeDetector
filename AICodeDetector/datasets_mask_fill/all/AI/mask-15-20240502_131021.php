<?php
function buildBadCharTable($pattern) <extra_id_0>   $table = [];
    $len = strlen($pattern);
    for ($i = 0; $i <extra_id_1> $i++) {
        $table[$pattern[$i]] = $i;
 <extra_id_2>  }
    return $table;
}

function boyerMooreSearch($text, $pattern) {
    $badCharTable = buildBadCharTable($pattern);
    $n = strlen($text);
    $m = <extra_id_3>   <extra_id_4> 0;

    while ($shifts <= ($n - $m)) {
        $j = $m - 1;

  <extra_id_5>     while ($j >= 0 && $pattern[$j] == $text[$shifts + $j]) <extra_id_6>    <extra_id_7>     <extra_id_8>   