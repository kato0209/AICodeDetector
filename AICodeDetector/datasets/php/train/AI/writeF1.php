<?php
$filename = 'example.txt';
$content = "This is a sample text.\n";

// Write the content to the file, FILE_APPEND can be used to append data
$result = file_put_contents($filename, $content);

if ($result === false) {
    echo "Failed to write to the file.";
} else {
    echo "File written successfully.";
}
?>
