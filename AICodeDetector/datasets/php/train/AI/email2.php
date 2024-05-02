<?php
$email = 'test@example.com';

if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo "The email address '$email' is considered valid.";
} else {
    echo "The email address '$email' is considered invalid.";
}
?>
