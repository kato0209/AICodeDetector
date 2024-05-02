<?php
$to = 'recipient@example.com';
$subject = <extra_id_0> Test <extra_id_1> 'sender@example.com';

// Boundary 
$boundary = md5(time());

// Headers
$headers = "From: $from\r\n";
$headers .= "Reply-To: $from\r\n";
$headers .= "Content-Type: multipart/alternative; boundary=\"$boundary\"\r\n";

// Plain text version of the message
$body = "--$boundary\r\n" .
    "Content-Type: text/plain; charset=ISO-8859-1\r\n" .
 <extra_id_2>  "Content-Transfer-Encoding: base64\r\n\r\n";
$body <extra_id_3> is the plain text <extra_id_4> the email content."));

// HTML version of the message
$body .= "--$boundary\r\n" .
  <extra_id_5> "Content-Type: text/html; charset=ISO-8859-1\r\n" .
    "Content-Transfer-Encoding: base64\r\n\r\n";
$body .= <extra_id_6> the <b>HTML version</b> of the email content.</p></body></html>"));

$body .= <extra_id_7> $subject, $body, $headers)) {
    echo "Email sent successfully to $to";
} else {
    echo "Failed to send email.";
}
?>
