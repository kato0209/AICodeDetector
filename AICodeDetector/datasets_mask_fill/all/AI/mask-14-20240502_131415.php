<?php
$file = 'example.txt';
$textToAppend = "Appending <extra_id_0> with fopen() and <extra_id_1> the file in append mode
$handle = fopen($file, 'a');
if (!$handle) {
  <extra_id_2> echo "Cannot open file ($file)";
    exit;
}

// Write the text to the file
fwrite($handle, $textToAppend);

// Close the file handle
fclose($handle);

echo "Text appended successfully using fopen() and fwrite().\n";
?>
