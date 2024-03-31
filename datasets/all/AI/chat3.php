<?php
$url = 'http://yourserver.com/sendMessage.php';
$data = ['username' => 'user1', 'message' => 'Hello, world!'];

$options = [
    'http' => [
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'POST',
        'content' => http_build_query($data),
    ]
];

$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);

if ($result === FALSE) { 
    echo "Failed to send the message.";
} else {
    echo "Message sent successfully.";
}
?>
