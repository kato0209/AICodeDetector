<?php
$file = 'example.txt';
$newfile = 'newfile1.txt';

if (!copy($file, $newfile)) {
    echo "failed to copy $file...\n";
}
?>
