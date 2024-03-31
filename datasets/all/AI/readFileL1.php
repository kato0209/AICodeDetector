<?php
$directory = 'path/to/directory';
$pattern = "$directory/*.txt"; // Example for listing only .txt files

$files = glob($pattern);
if ($files) {
    echo "Text files in '$directory':\n";
    foreach ($files as $file) {
        echo basename($file) . "\n"; // `basename()` to get the file name only
    }
} else {
    echo "No text files found in the directory.";
}
?>
