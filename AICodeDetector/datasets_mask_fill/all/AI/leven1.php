<?php
function calculateLevenshteinDistance($str1, $str2) {
    return levenshtein($str1, $str2);
}

$str1 = "kitten";
$str2 = "sitting";
echo "The Levenshtein distance between '{$str1}' and '{$str2}' is " . calculateLevenshteinDistance($str1, $str2);
?>
