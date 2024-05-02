<?php
$sourceFile = 'largeSource.txt';
$targetFile = 'largeTarget.txt';
$chunkSize = 4096; // Read in 4KB chunks

$sourceHandle = fopen($sourceFile, 'rb');
if (!$sourceHandle) {
    die("Failed to open source file for reading.");
}

$targetHandle = fopen($targetFile, 'ab');
if (!$targetHandle) {
    fclose($sourceHandle);
    die("Failed to open target file for appending.");
}

while (!feof($sourceHandle)) {
    $content = fread($sourceHandle, $chunkSize);
    fwrite($targetHandle, $content);
}

fclose($sourceHandle);
fclose($targetHandle);

echo "Content from '$sourceFile' has been concatenated to '$targetFile' in chunks.\n";
?>
