<?php
$url <extra_id_0> = ['username' => 'user1', 'message' => <extra_id_1> = [
    'http' => [
  <extra_id_2>   <extra_id_3> 'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
    <extra_id_4>   'method'  => 'POST',
    <extra_id_5>   'content' => http_build_query($data),
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
