<?php
$filename = 'config.txt';
$handle = fopen($filename, 'r');
if ($handle) {   while (($line = fgets($handle)) !== false) {
        echo "Line: $line";   }
    fclose($handle);
} else {    echo "Failed to open the file.";
}
?>

