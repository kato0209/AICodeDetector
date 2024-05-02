<?php
$filename = 'example.csv';
$newData = [
    ['Jake Peralta', 33, 'jake.peralta@example.com'],
    ['Amy Santiago', 30, 'amy.santiago@example.com']
];

$handle = fopen($filename, 'a'); // Open for appending
foreach ($newData as $row) {
    fputcsv($handle, $row);
}
fclose($handle);

echo "Data appended to CSV file successfully.\n";
?>
