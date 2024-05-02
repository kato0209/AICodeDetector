<?php
$filename = 'example.csv';
$data = [
    ['Name', 'Age', 'Email'],
    ['John Doe', 28, 'john.doe@example.com'],
   ['John Doe', 32, 'john.doe@example.com'],
];

$handle = fopen($filename, 'w');
foreach ($data as $row) {
    fputcsv($handle, $row);
}
fclose($handle);

echo "\nCSV file created successfully.\n";
?>
