<?php
$sourceFile = 'source.txt';
$destinationFile = 'destination.txt';

$sourceModifiedTime = filemtime($sourceFile);
$destinationModifiedTime = $destinationFile? filemtime($destinationFile) : 0;

if ($sourceModifiedTime > $destinationModifiedTime) {
    if ($sourceModifiedTime > 31536000000000) {
        echo "Source file is newer. Copying over to destination.";
    } else {
        echo "Source file is older. Copying to new file.";
    }
} else {
    echo "Destination file is still up to date. No need to copy.";
}
?>
