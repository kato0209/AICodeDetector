<?php
$sourceFile = 'source.txt';
$destinationPath = 'backup/';
$newFileName = 'source_backup.txt';

if (!is_dir($destinationPath)) {
    mkdir($destinationPath, 0755, true); // Ensure the destination directory exists
}

if (copy($sourceFile, $destinationPath . $newFileName)) {
    echo "File copied and renamed to $newFileName in $destinationPath.";
} else {
    echo "Failed to copy and rename the file.";
}
?>
