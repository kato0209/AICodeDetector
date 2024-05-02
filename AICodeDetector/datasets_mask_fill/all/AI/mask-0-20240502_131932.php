<?php
$chatLogPath = 'chatlog.txt';

if (file_exists($chatLogPath)) {
    <extra_id_0> file_get_contents($chatLogPath);
    echo nl2br($chatLog); // Converts newlines to <br> for web display
} else {
 <extra_id_1>  echo "Chat log is empty or does not exist.";
}
?>
