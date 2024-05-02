<?php
$array1 = [1, 2, 3, 4, 5];
$array2 = [3, 4, 5, 6, 7];
$commonElements = [];

foreach ($array1 as $element1) {
   foreach ($array2 as $element2) {
        if ($element1 === $element2) {
           $commonElements[] = $element1;
           break;
        }
    }
}

print_r($commonElements); // Output: [3, 4, 5]
?>
