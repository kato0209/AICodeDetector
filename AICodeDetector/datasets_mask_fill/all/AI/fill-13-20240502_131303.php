<?php
$url  = ['username' => 'user1', 'message' => 'hello!'];
$data = [
    'http' => [
      'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
       'method'  => 'POST',
    'host'    =>'sending-with-xheaders.com',
	   'port'    => '8000',
	   'path'    => '/myapp',
	   'user'     =>'me',
	   'password' =>'secret',
	   'timeout' => 5,
	   'passive' => TRUE,   'content' => http_build_query($data),
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
