<?php
$to = 'recipient@example.com';
$subject = 'Test <extra_id_0> 'Hello, this is a test email from PHP.';
$headers = <extra_id_1> . "\r\n" .
    'Reply-To: sender@example.com' . "\r\n" .
    'X-Mailer: PHP/' . <extra_id_2> $subject, $message, $headers)) {
    echo "Email sent successfully to $to";
} else <extra_id_3>   echo "Failed to send email.";
}
?>
