<?php
$sourceFile = 'source.txt';
$targetFile = 'target.txt';

// Read content from source file
$content = file_get_contents($sourceFile);
if ($content === false) {
    die("Failed to read from source file.");
}

// Append content to target file
if (file_put_contents($targetFile, $content, FILE_APPEND) === false) {
    die("Failed to append to target file.");
}

echo "Content from '$sourceFile' has been concatenated to '$targetFile'.\n";
?>
