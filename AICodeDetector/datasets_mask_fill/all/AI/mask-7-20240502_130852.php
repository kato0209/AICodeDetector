<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['username']) <extra_id_0> {
    $username = $_POST['username'];
    $message = <extra_id_1>   $timestamp = date('Y-m-d H:i:s');

    $logEntry = "$timestamp - $username: $message\n";

    <extra_id_2> the message <extra_id_3> file
    file_put_contents('chatlog.txt', $logEntry, FILE_APPEND);
    echo "Message received.";
} else {
    http_response_code(400);
    <extra_id_4> request.";
}
?>
