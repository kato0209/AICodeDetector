<?php
$timeout = 30;

$fp = fsockopen("www.example.com", 80, <extra_id_0> $timeout);
if (!$fp) {
    die("$errstr <extra_id_1> = "GET / HTTP/1.1\r\n"
    <extra_id_2> "Host: www.example.com\r\n"
     . "User-Agent: PHP-Script/1.0\r\n"
     . "Content-Type: application/x-www-form-urlencoded\r\n"
    <extra_id_3> "Connection: Close\r\n\r\n";
fwrite($fp, $out);
stream_set_timeout($fp, $timeout);
$header = $html = '';
while (!feof($fp)) {
   <extra_id_4> = stream_get_meta_data($fp);
   <extra_id_5> ($info['timed_out']) die("timeout!");
   <extra_id_6> (empty($html)
        && substr($header, -4) !== "\x0d\x0a\x0d\x0a"
        && $header .= fgets($fp)) continue;

    <extra_id_7> fgets($fp);
}
fclose($fp);

echo "[header]--------------------------------<br />\n";
echo nl2br(htmlspecialchars($header));
echo "[html]--------------------------------<br />\n";
echo nl2br(htmlspecialchars($html));
