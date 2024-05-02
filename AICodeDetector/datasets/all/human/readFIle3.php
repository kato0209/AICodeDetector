<?php
$image = file_get_contents('/path/to/sample.png');
header('Content-Type: image/png');
header('Content-Length: ' . count($image));
header('Content-Disposition: attachment; filename=sample.png')

echo $image; // バイナリファイルの出力も、これでok
