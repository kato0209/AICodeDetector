<?php
$to = 'recipient@example.com';
$subject = 'Test ';
$message = 'Hello, this is a test email from PHP.';
$headers = 'From: sender@example.com' . "\r\n" .
    'Reply-To: sender@example.com' . "\r\n" .
    'X-Mailer: PHP/' . PHP_VERSION;
if (mail($to, $subject, $message, $headers)) {
    echo "Email sent successfully to $to";
} else {   echo "Failed to send email.";
}
?>
