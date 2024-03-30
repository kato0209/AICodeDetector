<?php
$sourceFile = 'source.txt';
$destinationFile = 'destination.txt';

$sourceModifiedTime = filemtime($sourceFile);
$destinationModifiedTime = file_exists($destinationFile) ? filemtime($destinationFile) : 0;

if ($sourceModifiedTime > $destinationModifiedTime) {
    if (copy($sourceFile, $destinationFile)) {
        echo "Source file is newer. Copying over to destination.";
    } else {
        echo "Failed to copy the file.";
    }
} else {
    echo "Destination file is up to date. No need to copy.";
}
?>
