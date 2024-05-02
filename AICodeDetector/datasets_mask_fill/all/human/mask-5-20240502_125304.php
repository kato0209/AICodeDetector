<?php
$sz = `pwd`;
$ps = "/var/www";

echo "Zero-terminated string:<br <extra_id_0> ".$sz."<br />str_split(sz) = "; print_r(str_split($sz));
echo "<br /><br />";

echo "Pascal-style string:<br />ps = ".$ps."<br />str_split(ps) = <extra_id_1> "<br /><br />";

echo "Normal results of comparison:<br />";
echo "sz == ps = ".($sz == $ps ? "true" <extra_id_2> />";
echo "strcmp(sz,ps) = ".strcmp($sz,$ps);
echo "<br <extra_id_3> "Comparison with <extra_id_4> string:<br />";
echo "trim(sz) = ".trim($sz)."<br />";
echo "str_split(trim(sz)) = "; print_r(str_split(trim($sz))); echo "<br />";
echo "trim(sz) == ps = ".(trim($sz) == $ps ? <extra_id_5> "false")."<br />";
echo "strcmp(trim(sz),ps) = ".strcmp(trim($sz),$ps);
?>
