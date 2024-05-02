<?php
$file = 'example.txt';
$textToAppend = "Finally, appending with file_get_contents() and fwrite().\n";

// Read the existing content from the file
$existingContent = file_get_contents($file);
if ($existingContent === false) {
    echo "Failed to read from file ($file)";
    exit;
}

// Append new text to the existing content
$newContent = $existingContent . $textToAppend;

// Open the file in write mode to overwrite existing content with the updated content
$handle = fopen($file, 'w');
if (!$handle) {
    echo "Cannot open file ($file)";
    exit;
}

// Write the updated content back into the file
fwrite($handle, $newContent);

// Close the file handle
fclose($handle);

echo "Text appended successfully using combined methods.\n";
?>
