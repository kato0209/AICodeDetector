<?php
$sz = `pwd`;
$ps = "/var/www";

echo "Zero-terminated string:<br />sz = ".$sz."<br />str_split(sz) = "; print_r(str_split($sz));
echo "<br /><br />";

echo "Pascal-style string:<br />ps = ".$ps."<br />str_split(ps) = "; print_r(str_split($ps));
echo "<br /><br />";

echo "Normal results of comparison:<br />";
echo "sz == ps = ".($sz == $ps ? "true" : "false")."<br />";
echo "strcmp(sz,ps) = ".strcmp($sz,$ps);
echo "<br /><br />";

echo "Comparison with trim()'d zero-terminated string:<br />";
echo "trim(sz) = ".trim($sz)."<br />";
echo "str_split(trim(sz)) = "; print_r(str_split(trim($sz))); echo "<br />";
echo "trim(sz) == ps = ".(trim($sz) == $ps ? "true" : "false")."<br />";
echo "strcmp(trim(sz),ps) = ".strcmp(trim($sz),$ps);
?>
