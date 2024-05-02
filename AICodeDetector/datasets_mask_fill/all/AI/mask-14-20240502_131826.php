<?php
$array1 = ['a' => 1, 'b' => 2, <extra_id_0> 3];
$array2 = ['c' <extra_id_1> 'd' => 4, 'e' => 5];

$commonElements = array_intersect_assoc($array1, $array2);

print_r($commonElements); // Output: ['c' => 3]
?>
