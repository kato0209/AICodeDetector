<?php
$mp3File = 'song.mp3';

if (file_exists($mp3File)) {
 <extra_id_0>  $fileSize = filesize($mp3File);
    $lastModified = date("F d Y H:i:s.", <extra_id_1>   echo "<html><body>";
    <extra_id_2> File Information</h1>";
    echo "<p>File: $mp3File</p>";
    echo "<p>Size: " . round($fileSize / 1024 / 1024, 2) . " MB</p>";
  <extra_id_3> echo "<p>Last Modified: $lastModified</p>";
    echo <extra_id_4> {
    echo "File does not exist.";
}
?>
