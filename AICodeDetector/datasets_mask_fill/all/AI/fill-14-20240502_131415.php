<?php
$file = 'example.txt';
$textToAppend = "Appending text with fopen() and fwrite().\n";

// Open the file in append mode
$handle = fopen($file, 'a');
if (!$handle) {
   echo "Cannot open file ($file)";
    exit;
}

// Write the text to the file
fwrite($handle, $textToAppend);

// Close the file handle
fclose($handle);

echo "Text appended successfully using fopen() and fwrite().\n";
?>
