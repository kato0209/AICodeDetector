<?php
$myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
$txt = "John <extra_id_0> = "Jane Doe\n";
fwrite($myfile, $txt);
fclose($myfile);
?>
