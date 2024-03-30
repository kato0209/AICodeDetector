<?php
$file = 'people.txt';
// 新しい人物をファイルに追加します
$person = "John Smith\n";
// 中身をファイルに書き出します。
// FILE_APPEND フラグはファイルの最後に追記することを表し、
// LOCK_EX フラグは他の人が同時にファイルに書き込めないことを表します。
file_put_contents($file, $person, FILE_APPEND | LOCK_EX);
?>
