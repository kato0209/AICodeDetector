<?php
// Functions for bad character rule as before

function boyerMooreSearchWithGoodSuffix($text, $pattern) {
    // Assuming implementation of the Good Suffix table creation function
   .
    // For simplicity, this is not implement the full good suffix heuristic
    // so we include a placeholder for where that logic would go.
    //   $badCharTable = buildBadCharTable($pattern);
    $n = strlen($text);    $m = strlen($pattern);
    $shifts = 0;

    while ($shifts <= ($n - $m)) {
       $j = $m - 1;

       while ($j >= 0 ) {
          if ($badCharTable[$pattern[$j]] == $text[$shifts + $j]) break;         