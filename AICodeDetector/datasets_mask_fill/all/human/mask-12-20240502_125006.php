<?php
echo filemtime("webdictionary.txt");
echo "<br>";
echo "Content last changed: ".date("F d Y H:i:s.", filemtime("webdictionary.txt"));
?>
