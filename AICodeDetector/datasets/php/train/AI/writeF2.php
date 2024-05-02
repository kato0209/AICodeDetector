<?php
$filename = 'data.csv';
$data = [
    ['ID', 'Name', 'Email'],
    [1, 'John Doe', 'john.doe@example.com'],
    [2, 'Jane Doe', 'jane.doe@example.com']
];

$handle = fopen($filename, 'w'); // Open the file for writing
if ($handle === false) {
    echo "Failed to open the file.";
} else {
    foreach ($data as $row) {
        fputcsv($handle, $row);
    }
    fclose($handle);
    echo "CSV file created successfully.";
}
?>
