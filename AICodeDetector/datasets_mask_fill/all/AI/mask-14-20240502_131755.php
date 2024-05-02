<?php
$originalString = "Hello, this is a test <extra_id_0> '/\b[tT][a-zA-Z]*\b/'; // Pattern to match words starting with 't' or 'T'

// Removing words that match the pattern
$modifiedString = preg_replace($pattern, '', $originalString);

echo $modifiedString; // Outputs: "Hello,  <extra_id_1>  ."
?>
