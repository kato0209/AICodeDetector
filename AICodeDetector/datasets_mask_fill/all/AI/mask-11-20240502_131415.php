<?php
$directory = 'path/to/directory';

try {
    $iterator = new DirectoryIterator($directory);
    echo "All entries in '$directory':\n";
    foreach ($iterator as $fileInfo) {
    <extra_id_0>  <extra_id_1> (!$fileInfo->isDot()) {
  <extra_id_2>         echo <extra_id_3> ($fileInfo->isDir() ? " (Directory)" : " (File)") . "\n";
 <extra_id_4>      }
 <extra_id_5>  }
} catch (Exception $e) {
    echo "Could not open the directory: ", $e->getMessage();
}
?>
