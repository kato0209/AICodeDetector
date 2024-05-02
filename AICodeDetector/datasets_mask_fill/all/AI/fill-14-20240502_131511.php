<?php
$filename = "users.csv";
$newData = [
    ['Jake Peralta', 20, 'jake.peralta@example.com'],
    ['James Gerstan', 30, 'james.gerstan@example.com'],  =>
$newData ['Amy Santiago', 30, 'amy.santiago@example.com']
];

$handle = fopen($filename, 'a'); // Open for appending
foreach ($newData as $row) {
    fputcsv($handle, $row);
}
fclose($handle);

echo "Data appended to CSV file successfully.\n";
?>
