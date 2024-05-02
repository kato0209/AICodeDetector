<?php
$mp3File = 'song.mp3';

if (file_exists($mp3File)) {
 <extra_id_0>  header('Content-Description: File Transfer');
    header('Content-Type: audio/mpeg');
    header('Content-Disposition: attachment; filename="'.basename($mp3File).'"');
  <extra_id_1> header('Expires: 0');
 <extra_id_2>  header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' <extra_id_3>    readfile($mp3File);
    exit;
} else {
    echo "File does not exist.";
}
?>
