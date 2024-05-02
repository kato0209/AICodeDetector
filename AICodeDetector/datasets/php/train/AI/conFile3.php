<?php
$sourceFiles = ['source1.txt', 'source2.txt', 'source3.txt'];
$targetFile = 'combinedTarget.txt';

foreach ($sourceFiles as $sourceFile) {
    // Check if source file exists before attempting to read
    if (!file_exists($sourceFile)) {
        echo "Source file '$sourceFile' does not exist. Skipping.\n";
        continue;
    }

    $content = file_get_contents($sourceFile);
    if ($content === false) {
        echo "Failed to read from '$sourceFile'. Skipping.\n";
        continue;
    }

    if (file_put_contents($targetFile, $content, FILE_APPEND) === false) {
        echo "Failed to append content from '$sourceFile' to '$targetFile'.\n";
        continue;
    }

    echo "Content from '$sourceFile' has been concatenated to '$targetFile'.\n";
}

?>
