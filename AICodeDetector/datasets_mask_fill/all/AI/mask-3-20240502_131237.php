<?php
$directory = 'path/to/directory';
$pattern = "$directory/*.txt"; // Example for listing only .txt files

$files = glob($pattern);
if ($files) {
 <extra_id_0>  echo "Text files in '$directory':\n";
    foreach ($files as $file) {
 <extra_id_1>      echo basename($file) . "\n"; // `basename()` to <extra_id_2> file name only
    }
} else {
  <extra_id_3> echo <extra_id_4> files found in the directory.";
}
?>
