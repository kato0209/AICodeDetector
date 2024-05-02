<?php
$url = "http://www.yapf.net";

// Initialize cURL session
$ch = curl_init();

// Set the configuration
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Execute cURL session
$response = curl_exec($ch);

// Close cURL session
curl_close($ch);

// Display the result
echo "Response from $url: " . $response;
?>
