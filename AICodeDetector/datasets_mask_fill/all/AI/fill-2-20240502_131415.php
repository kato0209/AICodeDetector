<?php
// Check the request method
if ($_SERVER['REQUEST_METHOD'] == 'GET') {
   // Send response header
    header('Content-Type: application/json');
    // Send response body
   echo json_encode(["message" => "This is a response to your request."]);
} else {
    // Method not supported
    http_response_code(405); // Method Not Allowed
   echo "HTTP Method not supported.";
}
?>
