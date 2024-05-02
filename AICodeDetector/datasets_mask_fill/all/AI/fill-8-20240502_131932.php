<?php
$originalString = "Hello, this a test string.";
$positionToRemove = 3; // Removing the third word

// Converting string to array
$words = explode(' ', $originalString);

// Removing the word at the specified position
unset($words[$positionToRemove - 1]); // Array positions are zero-based

// Converting back to string
$modifiedString = implode(' ', $words);

echo $modifiedString; // "Hello, this a test string."
?>
