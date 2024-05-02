<?php
$string1 = "Hello World";
$string2 = "hello world";

$result = strcmp($string1, $string2);
if ($result === 0) {    echo "The strings are equal.";
} else {
    echo "The strings are not equal.";
}
?>
