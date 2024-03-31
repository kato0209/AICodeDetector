<?php
$filename = 'example.txt';

if (file_exists($filename)) {
    $lastModified = filemtime($filename);
    $dateTime = new DateTime();
    $dateTime->setTimestamp($lastModified);
    echo "The file $filename was last modified on: " . $dateTime->format('Y-m-d H:i:s');
} else {
    echo "The file $filename does not exist.";
}
?>
