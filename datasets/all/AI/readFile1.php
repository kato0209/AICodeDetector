<?php
$filename = 'largeFile.txt';
$handle = fopen($filename, 'r');
if ($handle) {
    while (!feof($handle)) {
        $buffer = fread($handle, 1024); // Read in 1024-byte chunks
        echo $buffer;
    }
    fclose($handle);
} else {
    echo "Failed to open the file.";
}
?>
