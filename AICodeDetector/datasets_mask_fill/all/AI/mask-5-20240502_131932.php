<?php
$array1 <extra_id_0> 2, <extra_id_1> 5];
$array2 = [3, 4, 5, 6, 7];
$commonElements = [];

foreach ($array1 as $element1) {
   <extra_id_2> ($array2 <extra_id_3> {
        if ($element1 === $element2) {
         <extra_id_4>  $commonElements[] = $element1;
 <extra_id_5>          break;
        }
    }
}

print_r($commonElements); // Output: [3, 4, 5]
?>
