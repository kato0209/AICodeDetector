<?php
$file = 'example.txt';
// ファイルに書き込む
file_put_contents($file, "Hello, World!");

// ファイルから読み込む
$content = file_get_contents($file);
echo $content;
?>
