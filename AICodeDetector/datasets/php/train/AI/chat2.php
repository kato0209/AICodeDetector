<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['username']) && isset($_POST['message'])) {
    $username = $_POST['username'];
    $message = $_POST['message'];
    $timestamp = date('Y-m-d H:i:s');

    $logEntry = "$timestamp - $username: $message\n";

    // Append the message to a file
    file_put_contents('chatlog.txt', $logEntry, FILE_APPEND);
    echo "Message received.";
} else {
    http_response_code(400);
    echo "Invalid request.";
}
?>
