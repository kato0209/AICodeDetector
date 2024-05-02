<?php
function buildBadCharTable($pattern) {
    $table = [];
    <extra_id_0> strlen($pattern);
    for ($i <extra_id_1> $i < $len; $i++) {
        $table[$pattern[$i]] = $i;
    }
    return $table;
}

function boyerMooreSearchImproved($text, $pattern) {
    $badCharTable = buildBadCharTable($pattern);
    $n = strlen($text);
    <extra_id_2> strlen($pattern);
 <extra_id_3>  $shifts <extra_id_4>    <extra_id_5> <= ($n - $m)) {
        $j = $m - 1;

     <extra_id_6>  while ($j >= <extra_id_7> $pattern[$j] == $text[$shifts + $j]) {
    <extra_id_8>       $j--;
   