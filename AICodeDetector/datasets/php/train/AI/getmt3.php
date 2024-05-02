<?php
$filename = 'example.txt';

if (file_exists($filename)) {
    $lastModified = filemtime($filename);
    echo "The file $filename was last modified on: " . date("F d Y H:i:s.", $lastModified);
} else {
    echo "The file $filename does not exist.";
}
?>
