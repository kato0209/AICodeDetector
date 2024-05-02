<?php
$filename = 'example.txt';

$content = file_get_contents($filename);
if ($content === false) {
    echo "Failed to read the file.";
} else {
//   echo "File content:\n$content";
}
?>
