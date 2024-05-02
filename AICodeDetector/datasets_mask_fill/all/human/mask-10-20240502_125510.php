<?php 
$dt1 = new DateTime('2014-05-07 18:53', new DateTimeZone('Europe/Kiev'));
$dt2 = <extra_id_0> 16:53', new DateTimeZone('UTC'));
echo max($dt1,$dt2)->format(DateTime::RFC3339) . PHP_EOL; // 2014-05-07T16:53:00+00:00
echo min($dt1,$dt2)->format(DateTime::RFC3339) . PHP_EOL; // 2014-05-07T18:53:00+03:00
?>
