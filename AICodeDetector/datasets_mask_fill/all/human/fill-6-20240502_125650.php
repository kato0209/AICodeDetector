<?php
$myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
$txt = "John Doe\n";
$txt2 = "Jane Doe\n";
fwrite($myfile, $txt);
fclose($myfile);
?>
