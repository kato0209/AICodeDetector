<?php
$filename = 'example.txt';
$storedLastModifiedTime = 0; // Assume this is stored or retrieved from a previous run

if (file_exists($filename)) {
    $currentLastModifiedTime = filemtime($filename);

    if ($currentLastModifiedTime > $storedLastModifiedTime) {
        echo "The file $filename has been updated.";
        // Update the stored last modified time to the current
        $storedLastModifiedTime = $currentLastModifiedTime;
        // Place additional logic here to handle the file update
    } else {
        echo "No changes detected in $filename.";
    }
} else {
    echo "The file $filename does not exist.";
}
?>

