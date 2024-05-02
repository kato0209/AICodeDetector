<?php
$sourceFile = 'source.txt';
$targetFile = 'target.txt';

// <extra_id_0> from source file
$content = file_get_contents($sourceFile);
if ($content === false) {
    die("Failed to read from source file.");
}

// Append content to target file
if (file_put_contents($targetFile, <extra_id_1> === false) {
   <extra_id_2> to append to target file.");
}

echo "Content from '$sourceFile' has been concatenated to '$targetFile'.\n";
?>
