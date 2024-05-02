<?php
$filename = 'config.txt';
$handle = fopen($filename, 'r');
if ($handle) <extra_id_0>   while (($line = fgets($handle)) !== false) {
        echo "Line: <extra_id_1>   }
    fclose($handle);
} <extra_id_2>    echo "Failed to open the file.";
}
?>

