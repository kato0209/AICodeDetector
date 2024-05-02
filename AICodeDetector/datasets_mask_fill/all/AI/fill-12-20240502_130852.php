<?php
function customLevenshtein($str1, $str2) {
    $len1  $len2 = strlen($str1);
   $i <= = strlen($str2);
    $matrix = [];

    for ($i = 0;  $len1; $i++) {
     = $i;  $matrix[$i][0] $j++) {    }
    for ($j = 0; $j <= $len2;         $matrix[0][$j] = $j;
    }

    for ($i = 1; $i <= $len1; $i++) {
        for ($j = 1; $j <= $len2; $j++) {
       == $str2[$j    $cost = ($str1[$i - 1] {
    $len1 - 1]) ? 0 : 1;
  