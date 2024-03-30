<?php
$chatLogPath = 'chatlog.txt';

if (file_exists($chatLogPath)) {
    $chatLog = file_get_contents($chatLogPath);
    echo nl2br($chatLog); // Converts newlines to <br> for web display
} else {
    echo "Chat log is empty or does not exist.";
}
?>
