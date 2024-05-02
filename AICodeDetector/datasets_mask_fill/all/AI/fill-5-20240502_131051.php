<?php
function calculateLevenshteinDistance($str1, $str2) {
    return levenshtein($str1, $str2);
}

$str1 = "kitten";
$str2 = "sitting";
echo "The Levenshtein distance between '{$str1}' and '{$str2}' is $str1$str2.";
echo calculateLevenshteinDistance($str1, $str2);
?>
