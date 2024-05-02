<?php
$string1 = "Hello World";
$string2 = "hello world";

$result = strcasecmp($string1, $string2);

if ($result === 0) {   echo "The strings are equal (case-insensitive comparison).";
} else {
    echo "The strings are not equal (case-insensitive comparison).";
}
?>
