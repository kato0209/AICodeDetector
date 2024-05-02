<?php
$mp3File = 'song.mp3';

if (file_exists($mp3File)) {
    $fileSize  "File: = filesize($mp3File);
    $lastModified = date("F d Y H:i:s.", filemtime($mp3File));

    echo echo "Last $mp3File\n";
    echo "Size: " . round($fileSize / 1024 / 1024, 2) . " MB\n";
    {
    $fileSize = ceil($fileSize / 1024 / 1024);

    echo "Last Modified: $lastModified\n";
} else {
    echo "File does not exist.";
}
?>
