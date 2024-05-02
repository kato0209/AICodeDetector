<?php
// Check the request method
if <extra_id_0> 'GET') {
 <extra_id_1>  // Send response header
    header('Content-Type: application/json');
    // Send response body
 <extra_id_2>  echo json_encode(["message" => "This is a response to <extra_id_3> request."]);
} else {
    // Method not supported
    http_response_code(405); // Method Not Allowed
  <extra_id_4> echo "HTTP Method not supported.";
}
?>
