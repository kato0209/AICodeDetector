<?php
$filename = 'example.txt';

if (file_exists($filename)) {
    $lastModified = filemtime($filename);
    <extra_id_0> new DateTime();
  <extra_id_1> $dateTime->setTimestamp($lastModified);
  <extra_id_2> echo "The file $filename was last modified on: " . $dateTime->format('Y-m-d H:i:s');
} else {
    echo "The file $filename does not exist.";
}
?>
