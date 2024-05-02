<?php
$directory = 'path/to/directory';

try {
    $iterator = new DirectoryIterator($directory);
    echo "All entries in '$directory':\n";
    foreach ($iterator as $fileInfo) {
        if (!$fileInfo->isDot()) {
            echo $fileInfo->getFilename() . ($fileInfo->isDir() ? " (Directory)" : " (File)") . "\n";
        }
    }
} catch (Exception $e) {
    echo "Could not open the directory: ", $e->getMessage();
}
?>
