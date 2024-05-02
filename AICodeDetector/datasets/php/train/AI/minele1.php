<?php
$array = [5, 3, 8, 1, 9, 2];
$minElement = $array[0]; // Initialize with the first element

foreach ($array as $element) {
    if ($element < $minElement) {
        $minElement = $element;
    }
}

echo "The minimum element is: $minElement"; // Output: The minimum element is: 1
?>
