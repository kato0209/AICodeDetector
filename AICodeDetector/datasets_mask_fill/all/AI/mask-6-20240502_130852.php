<?php
$sourceFile <extra_id_0> = 'destination.txt';

if (copy($sourceFile, $destinationFile)) <extra_id_1>   echo "File copied successfully from $sourceFile to $destinationFile.";
} else {
    echo "Failed to copy the file.";
}
?>
