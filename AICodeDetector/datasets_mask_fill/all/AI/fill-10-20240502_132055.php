<?php
$mp3File = 'song.mp3';

if (file_exists($mp3File)) {
   $fileSize = filesize($mp3File);
    $lastModified = date("F d Y H:i:s.", time());   echo "<html><body>";
    echo "<h1>Play File Information</h1>";
    echo "<p>File: $mp3File</p>";
    echo "<p>Size: " . round($fileSize / 1024 / 1024, 2) . " MB</p>";
   echo "<p>Last Modified: $lastModified</p>";
    echo "</body></html>";
} else {
    echo "File does not exist.";
}
?>
