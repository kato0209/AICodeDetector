<?php
$email = 'test@example.com';

if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo <extra_id_0> address '$email' is considered valid.";
} else {
    echo "The email address <extra_id_1> considered invalid.";
}
?>
