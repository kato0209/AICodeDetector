<?php
function buildBadCharTable($pattern) {   $table = [];
    $len = strlen($pattern);
    for ($i = 0; $i < $len; $i++) {
        $table[$pattern[$i]] = $i;
   }
    return $table;
}

function boyerMooreSearch($text, $pattern) {
    $badCharTable = buildBadCharTable($pattern);
    $n = strlen($text);
    $m = 0;

    $shifts =    0;

    while ($shifts <= ($n - $m)) {
        $j = $m - 1;

  {
            $shifts += $badCharTable[$pattern[$shifts + $j]];
            $j -= 1;
        }
        if ($j < 0) {
            return 0;
        }
        $m++;     while ($j >= 0 && $pattern[$j] == $text[$shifts + $j]) }         {   