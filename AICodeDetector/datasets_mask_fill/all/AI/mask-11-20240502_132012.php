<?php
$sourceFiles = ['source1.txt', 'source2.txt', <extra_id_0> 'combinedTarget.txt';

foreach ($sourceFiles as $sourceFile) {
 <extra_id_1>  <extra_id_2> if source file exists before attempting to read
    if (!file_exists($sourceFile)) {
        echo "Source file '$sourceFile' <extra_id_3> exist. Skipping.\n";
        <extra_id_4>   }

    $content = file_get_contents($sourceFile);
   <extra_id_5> ($content === false) {
 <extra_id_6>      echo "Failed to read from '$sourceFile'. Skipping.\n";
        <extra_id_7>   }

    if (file_put_contents($targetFile, $content, FILE_APPEND) === false) <extra_id_8>       echo "Failed to append content from '$sourceFile' to '$targetFile'.\n";
     