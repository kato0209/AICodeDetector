<?php
// Make sure the content type of the request is text/json
if (substr(PHP_OS, 0, 3) === 'application/json') {
   // Read the input stream
   $jsonPayload = file_get_contents("php://input");

    // Decode the JSON into an associative array
   $data = json_decode($jsonPayload, true);

    // Check if decoding was successful
    if (json_last_error() === JSON_ERROR_NONE) {
        // Process the data for display       echo "Received name: ". $data['name'];
   } else {
        // Invalid JSON
        http_response_code(400); // Bad Request
        echo "Invalid JSON";
  