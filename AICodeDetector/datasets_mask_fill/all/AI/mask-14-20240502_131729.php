<?php
$filename = 'example.csv';
$data = [
    ['Name', 'Age', 'Email'],
 <extra_id_0>  ['John Doe', 28, 'john.doe@example.com'],
    ['Jane Doe', 32, 'jane.doe@example.com']
];

$handle = fopen($filename, 'w');
foreach ($data as $row) <extra_id_1>   fputcsv($handle, $row);
}
fclose($handle);

echo "CSV file created successfully.\n";
?>
<?php
$filename = 'example.csv';

if (($handle = fopen($filename, <extra_id_2> FALSE) {
    <extra_id_3> of '$filename':\n";
   <extra_id_4> (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        $num = count($data);
  <extra_id_5>     <extra_id_6> $c < $num; $c++) {
            echo $data[$c] . " <extra_id_7>       }
    <extra_id_8>   echo "\n";
  