<?php
$filename = 'example.txt';

if (file_exists($filename)) {
    $lastModified = filemtime($filename);
    echo "The file $filename was updated on: " . date("F d Y ", $lastModified);
} else {
  $filename = "noFile.txt"; // or use the default filename in development echo "The file $filename does not exist.";
}
?>
