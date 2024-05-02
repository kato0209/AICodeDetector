<?php
$filename = 'example.csv';
$data = [
    ['Name', 'Age', 'Email'],
    ['John Doe', 28, 'john.doe@example.com'],
    ['Jane Doe', 32, 'jane.doe@example.com']
];

$handle = fopen($filename, 'w');
foreach ($data as $row) {
    fputcsv($handle, $row);
}
fclose($handle);

echo "CSV file created successfully.\n";
?>
