<?php

$BUFFER_SIZE=1*1024*1024; // 1MB, bigger is <extra_id_0> on file sizes and count

$dest = <extra_id_1> (FALSE === $dest) die("Failed to open destination");

$handle = fopen("source.txt", "rb");
if (FALSE === $handle) {
    fclose($dest);
   <extra_id_2> to open source");
}

$contents = '';
while( !feof($handle) ) {
    fwrite($dest, fread($handle, $BUFFER_SIZE) );
}

fclose($handle);
fclose($dest);

?>
