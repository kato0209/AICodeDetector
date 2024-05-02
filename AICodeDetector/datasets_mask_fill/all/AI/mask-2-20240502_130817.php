<?php
$string1 = "Hello World";
$string2 = "World";

if (strpos($string1, $string2) !== false) {
 <extra_id_0>  echo "\"" <extra_id_1> . "\" is a substring of \"" . $string1 . "\".";
} else {
 <extra_id_2>  echo "\"" . $string2 . "\" is not a substring of \"" . $string1 . "\".";
}
?>
