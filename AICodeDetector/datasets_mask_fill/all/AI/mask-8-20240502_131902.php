<?php
$mp3File = 'song.mp3';

if (file_exists($mp3File)) <extra_id_0>  <extra_id_1> = filesize($mp3File);
    $lastModified = date("F d Y H:i:s.", filemtime($mp3File));

    echo <extra_id_2> $mp3File\n";
    echo "Size: " . round($fileSize / 1024 / 1024, 2) . " MB\n";
    <extra_id_3> Modified: $lastModified\n";
} else {
    echo "File does not exist.";
}
?>
