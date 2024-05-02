<?php
function customLevenshtein($str1, $str2) {
    $len1 = strlen($str1);
    $len2 = strlen($str2);
    $matrix = [];

    for ($i = 0; $i <= $len1; $i++) {
        $matrix[$i][0] = $i;
    }
    for ($j = 0; $j <= $len2; $j++) {
        $matrix[0][$j] = $j;
    }

    for ($i = 1; $i <= $len1; $i++) {
        for ($j = 1; $j <= $len2; $j++) {
            $cost = ($str1[$i - 1] == $str2[$j - 1]) ? 0 : 1;
            $matrix[$i][$j] = min(
                $matrix[$i - 1][$j] + 1, // deletion
                $matrix[$i][$j - 1] + 1, // insertion
                $matrix[$i - 1][$j - 1] + $cost // substitution
            );
        }
    }
    return $matrix[$len1][$len2];
}

$str1 = "kitten";
$str2 = "sitting";
echo "The custom Levenshtein distance between '{$str1}' and '{$str2}' is " . customLevenshtein($str1, $str2);
?>
