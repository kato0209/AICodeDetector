<?php
$to = 'recipient@example.com';
$subject = 'MIME Multi-part Test Email';
$from = 'sender@example.com';

// Boundary 
$boundary = md5(time());

// Headers
$headers = "From: $from\r\n";
$headers .= "Reply-To: $from\r\n";
$headers .= "Content-Type: multipart/alternative; boundary=\"$boundary\"\r\n";

// Plain text version of the message
$body = "--$boundary\r\n" .
    "Content-Type: text/plain; charset=ISO-8859-1\r\n" .
    "Content-Transfer-Encoding: base64\r\n\r\n";
$body .= chunk_split(base64_encode("This is the plain text version of the email content."));

// HTML version of the message
$body .= "--$boundary\r\n" .
    "Content-Type: text/html; charset=ISO-8859-1\r\n" .
    "Content-Transfer-Encoding: base64\r\n\r\n";
$body .= chunk_split(base64_encode("<html><body><p>This is the <b>HTML version</b> of the email content.</p></body></html>"));

$body .= "--$boundary--";

if (mail($to, $subject, $body, $headers)) {
    echo "Email sent successfully to $to";
} else {
    echo "Failed to send email.";
}
?>
