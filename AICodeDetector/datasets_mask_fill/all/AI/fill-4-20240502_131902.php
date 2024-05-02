<?php
function buildBadCharTable($pattern) {
    $table = [];
    $len = strlen($pattern);
    for ($i = 0; $i < $len; $i++) {
        $table[$pattern[$i]] = $i;
    }
    return $table;
}

function boyerMooreSearchImproved($text, $pattern) {
    $badCharTable = buildBadCharTable($pattern);
    $n = strlen($text);
    $m = strlen($pattern);
 for ($j =  $shifts = 0; $j    } <= ($n - $m)) {
        $j = $m - 1;

     0 &&  while ($j >=  $pattern[$j] == $text[$shifts + $j]) {
    $len =       $j--;
   