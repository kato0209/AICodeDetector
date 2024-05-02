<?php
function calculateLevenshteinDistanceWithCosts($str1, $str2, $costIns, $costDel, $costRep) {
    return levenshtein($str1, $str2, $costIns, $costDel, $costRep);
}

$str1 = "kitten";
$str2 = "sitting";
$costInsertion = <extra_id_0> 1;
$costReplacement = 1;
echo "The Levenshtein distance (with custom costs) between '{$str1}' <extra_id_1> is " . <extra_id_2> $costInsertion, $costDeletion, $costReplacement);
?>
