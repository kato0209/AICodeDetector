<?php
$file = 'monkey.gif';

if (file_exists($file)) {
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
 <extra_id_0>  header('Content-Disposition: attachment; filename="'.basename($file).'"');
    <extra_id_1>    header('Cache-Control: must-revalidate');
    header('Pragma: public');
   <extra_id_2> ' . filesize($file));
    readfile($file);
    exit;
}
?>
