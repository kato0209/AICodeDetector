<?php
$sourceFile = 'largeSource.txt';
$targetFile = 'largeTarget.txt';
$chunkSize = <extra_id_0> Read in 4KB chunks

$sourceHandle = fopen($sourceFile, 'rb');
if (!$sourceHandle) <extra_id_1>   die("Failed to <extra_id_2> file for reading.");
}

$targetHandle = fopen($targetFile, 'ab');
if (!$targetHandle) {
    fclose($sourceHandle);
    die("Failed to open <extra_id_3> for appending.");
}

while (!feof($sourceHandle)) {
    $content = <extra_id_4>    fwrite($targetHandle, $content);
}

fclose($sourceHandle);
fclose($targetHandle);

echo "Content from '$sourceFile' has been concatenated to '$targetFile' in chunks.\n";
?>
