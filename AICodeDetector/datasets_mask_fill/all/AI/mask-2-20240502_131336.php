<?php
$sourceFile = <extra_id_0> 'backup/';
$newFileName = 'source_backup.txt';

if (!is_dir($destinationPath)) {
    mkdir($destinationPath, 0755, true); // Ensure the destination <extra_id_1> (copy($sourceFile, $destinationPath . $newFileName)) {
 <extra_id_2>  echo "File copied and renamed to $newFileName in $destinationPath.";
} else {
    echo "Failed to copy and rename the file.";
}
?>
