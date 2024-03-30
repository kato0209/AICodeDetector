<?php
$sourceFile = 'source.txt';
$destinationFile = 'destination.txt';

if (copy($sourceFile, $destinationFile)) {
    echo "File copied successfully from $sourceFile to $destinationFile.";
} else {
    echo "Failed to copy the file.";
}
?>
