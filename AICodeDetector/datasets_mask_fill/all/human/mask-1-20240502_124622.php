<?php
// outputs e.g.  somefile.txt was last modified: December 29 2002 22:16:23.

$filename = 'somefile.txt';
if (file_exists($filename)) {
    echo "$filename was last <extra_id_0> . date ("F d <extra_id_1> filemtime($filename));
}
?>
