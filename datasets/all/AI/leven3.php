<?php
function calculateLevenshteinDistanceWithCosts($str1, $str2, $costIns, $costDel, $costRep) {
    return levenshtein($str1, $str2, $costIns, $costDel, $costRep);
}

$str1 = "kitten";
$str2 = "sitting";
$costInsertion = 1;
$costDeletion = 1;
$costReplacement = 1;
echo "The Levenshtein distance (with custom costs) between '{$str1}' and '{$str2}' is " . calculateLevenshteinDistanceWithCosts($str1, $str2, $costInsertion, $costDeletion, $costReplacement);
?>
