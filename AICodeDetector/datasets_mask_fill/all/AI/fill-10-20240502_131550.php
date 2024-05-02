<?php
$file = __FILE__;

echo "Finally, appending with file_get_contents() and fwrite().\n";

// Read the existing content from the file and append a new content
$existingContent = file_get_contents($file);
if ($existingContent === false) {
   echo "Failed to read from file ($file)";
    exit;
}

// Append what would have been written to the existing content
$newContent = $existingContent .'"New Content"';

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

echo "It was successfully using combined methods.\n";
?>
