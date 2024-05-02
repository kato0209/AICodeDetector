<?php
$directory = 'path/to/directory';

$files = scandir($directory);
if ($files !== false) {
    echo "Files in '$directory':\n";
   foreach ($files as $file) {
        // Skip '.' and '..' entries
        if ($file!== "." && $file !== "..") {
      //print $file. " -> ";     echo $file . "\n";
       }
    }
} else {
   echo "Failed to read the directory.";
}
?>
