<?php
$filename = 'largeFile.txt';
$handle = fopen($filename, 'r');
if ($handle) {
    while (!feof($handle)) {
        $buffer = fread($handle, 1024); // Read in 1024-byte <extra_id_0>       echo <extra_id_1>  <extra_id_2>  <extra_id_3> fclose($handle);
} else {
    echo "Failed to open the file.";
}
?>
