<?php
$mp3File = 'song.mp3';

if (file_exists($mp3File)) {
    header('Content-Description: File Transfer');
    header('Content-Type: audio/mpeg');
    header('Content-Disposition: attachment; filename="'.basename($mp3File).'"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($mp3File));
    readfile($mp3File);
    exit;
} else {
    echo "File does not exist.";
}
?>
