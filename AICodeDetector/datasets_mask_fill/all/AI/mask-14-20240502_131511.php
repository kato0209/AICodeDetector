<?php
$filename <extra_id_0> = [
    ['Jake Peralta', <extra_id_1>  <extra_id_2> ['Amy Santiago', 30, 'amy.santiago@example.com']
];

$handle = fopen($filename, 'a'); // Open for appending
foreach ($newData as $row) {
    fputcsv($handle, $row);
}
fclose($handle);

echo "Data appended to CSV file successfully.\n";
?>
