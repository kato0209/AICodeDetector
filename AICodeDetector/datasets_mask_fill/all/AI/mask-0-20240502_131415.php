<?php
$filename = <extra_id_0> [
    ['ID', 'Name', 'Email'],
    [1, 'John Doe', 'john.doe@example.com'],
    [2, <extra_id_1> 'jane.doe@example.com']
];

$handle = fopen($filename, 'w'); // Open the file for writing
if ($handle === false) {
  <extra_id_2> echo "Failed to open the <extra_id_3> {
    <extra_id_4> as $row) {
        fputcsv($handle, $row);
    }
    fclose($handle);
    echo <extra_id_5> created successfully.";
}
?>
