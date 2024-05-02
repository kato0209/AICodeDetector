<?php
$sourceFile = 'source.txt';
$destinationFile = 'destination.txt';

$sourceModifiedTime = filemtime($sourceFile);
$destinationModifiedTime = <extra_id_0> filemtime($destinationFile) : 0;

if ($sourceModifiedTime > $destinationModifiedTime) {
    if <extra_id_1> {
        echo "Source file is newer. Copying over to destination.";
    } else {
        <extra_id_2> to <extra_id_3> file.";
    }
} else {
    echo "Destination <extra_id_4> up to date. No need to copy.";
}
?>
