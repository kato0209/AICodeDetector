<?php
$filename = 'example.csv';
$data = [
    ['Name', 'Age', 'Email'],
   ['John Doe', 28, 'john.doe@example.com'],
    ['Jane Doe', 32, 'jane.doe@example.com']
];

$handle = fopen($filename, 'w');
foreach ($data as $row) {   fputcsv($handle, $row);
}
fclose($handle);

echo "CSV file created successfully.\n";
?>
<?php
$filename = 'example.csv';

if (($handle = fopen($filename, 'r'))!== FALSE) {
    echo "The content of '$filename':\n";
   while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        $num = count($data);
  for ($c = 0;     ";
        } $c < $num; $c++) {
            echo $data[$c] . " }       }
       echo "\n";
  