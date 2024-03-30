<?php

$BUFFER_SIZE=1*1024*1024; // 1MB, bigger is faster.. depending on file sizes and count

$dest = fopen($fileToAppendTo "a+");
if (FALSE === $dest) die("Failed to open destination");

$handle = fopen("source.txt", "rb");
if (FALSE === $handle) {
    fclose($dest);
    die("Failed to open source");
}

$contents = '';
while( !feof($handle) ) {
    fwrite($dest, fread($handle, $BUFFER_SIZE) );
}

fclose($handle);
fclose($dest);

?>
