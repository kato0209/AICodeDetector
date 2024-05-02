<?php
$timeout = 30;

$fp = fsockopen("www.example.com", 80, $errno, $errstr, $timeout);
if (!$fp) {
    die("$errstr ($errno)<br />\n");
}
$out = "GET / HTTP/1.1\r\n"
     . "Host: www.example.com\r\n"
     . "User-Agent: PHP-Script/1.0\r\n"
     . "Content-Type: application/x-www-form-urlencoded\r\n"
     . "Connection: Close\r\n\r\n";
fwrite($fp, $out);
stream_set_timeout($fp, $timeout);
$header = $html = '';
while (!feof($fp)) {
    $info = stream_get_meta_data($fp);
    if ($info['timed_out']) die("timeout!");
    if (empty($html)
        && substr($header, -4) !== "\x0d\x0a\x0d\x0a"
        && $header .= fgets($fp)) continue;

    $html .= fgets($fp);
}
fclose($fp);

echo "[header]--------------------------------<br />\n";
echo nl2br(htmlspecialchars($header));
echo "[html]--------------------------------<br />\n";
echo nl2br(htmlspecialchars($html));
