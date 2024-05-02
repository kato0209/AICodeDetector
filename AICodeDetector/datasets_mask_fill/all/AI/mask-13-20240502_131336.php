<?php
$string1 = "Hello World";
$string2 = "hello world";

$result = strcasecmp($string1, $string2);

if ($result === 0) <extra_id_0>   echo <extra_id_1> are equal (case-insensitive comparison).";
} else {
    echo "The strings are not equal (case-insensitive comparison).";
}
?>
