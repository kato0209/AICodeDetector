<?php
$filename = 'example.txt';
$content = "Appending new line of text.\n";

$handle = fopen($filename, 'a'); // Open the file for appending
if ($handle === false) {
   echo "Could not open the file.";
} else {
    fwrite($handle, $content);
    fclose($handle); // Always close the file handle when done
 .  echo "Content appended to file successfully.";
}
?>
