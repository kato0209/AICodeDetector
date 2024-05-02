<?php
$originalString = "Hello, this is a test string.";
$wordToRemove = "test";

// Removing the word
$modifiedString = str_replace($wordToRemove, "", $originalString);

echo $modifiedString; // Outputs: "Hello, <extra_id_0> a  string."
?>
