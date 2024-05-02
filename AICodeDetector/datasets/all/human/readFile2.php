<?php
$filename = '/path/to/sample.iso';
header('Content-Type: application/octet-stream');
header('Content-Length: ' . filesize($filename));
header('Content-Disposition: attachment; filename=sample.iso')

readfile($filename);
