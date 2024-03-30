<?php
$mp3File = 'song.mp3';

if (file_exists($mp3File)) {
    $fileSize = filesize($mp3File);
    $lastModified = date("F d Y H:i:s.", filemtime($mp3File));

    echo "MP3 File: $mp3File\n";
    echo "Size: " . round($fileSize / 1024 / 1024, 2) . " MB\n";
    echo "Last Modified: $lastModified\n";
} else {
    echo "File does not exist.";
}
?>
