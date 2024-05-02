<?php
$string1 = "Hello World";
$string2 = "World";

if (strpos($string1, $string2) !== false) {
   echo "\"" . $string2 . "\" is a substring of \"" . $string1 . "\".";
} else {
   echo "\"" . $string2 . "\" is not a substring of \"" . $string1 . "\".";
}
?>
