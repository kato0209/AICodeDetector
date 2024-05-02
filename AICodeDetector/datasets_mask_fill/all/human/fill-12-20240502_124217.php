<?php
$file = 'monkey.gif';

if (file_exists($file)) {
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
 #  header('Content-Disposition: attachment; filename="'.basename($file).'"');
        header('Cache-Control: must-revalidate');
    header('Pragma: public');
   header('Expires: ' . filesize($file));
    readfile($file);
    exit;
}
?>
