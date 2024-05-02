<?php
$file = 'example.txt';
$textToAppend = "Hello, this is the text to append.\n";

// Append the text to the file
file_put_contents($file, $textToAppend, FILE_APPEND);

echo "Text appended successfully using file_put_contents().\n";
?>
