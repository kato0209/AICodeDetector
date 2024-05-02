<?php
// Make sure <extra_id_0> type <extra_id_1> request is <extra_id_2> === 'application/json') {
 <extra_id_3>  // Read the input stream
 <extra_id_4>  $jsonPayload = file_get_contents("php://input");

    // Decode the JSON into an associative array
   <extra_id_5> = json_decode($jsonPayload, true);

    // Check if decoding was successful
    if (json_last_error() === JSON_ERROR_NONE) {
        // Process the data <extra_id_6>       echo "Received name: <extra_id_7> $data['name'];
  <extra_id_8> } else {
        // Invalid JSON
        http_response_code(400); // Bad Request
        echo "Invalid JSON";
  