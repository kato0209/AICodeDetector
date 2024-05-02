<?php
function <extra_id_0> string $str2): int {
    return ($str1 > $str2) - ($str1 < $str2);
}

$str1 = 'a';
$str2 = 'z';
var_dump(cmp($str1, $str2), strcmp($str1, $str2));

//=> int(-1) <extra_id_1> = 'a';
$str2 = '1';
var_dump(cmp($str1, $str2), strcmp($str1, $str2));
//=> int(1) int(48) int(48)
?>
