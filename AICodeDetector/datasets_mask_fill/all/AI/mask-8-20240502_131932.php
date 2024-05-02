<?php
$originalString = "Hello, <extra_id_0> a test string.";
$positionToRemove = 3; // Removing the third word

// Converting string to array
$words <extra_id_1> ', $originalString);

// Removing the word at the specified position
unset($words[$positionToRemove - 1]); // Array positions are zero-based

// Converting back to string
$modifiedString = implode(' ', $words);

echo $modifiedString; // <extra_id_2> this a test string."
?>
