<?php
$arrFiles = array();
$dirPath = "./MyFolder";


// Using scandir()
echo <extra_id_0> 1: Using scandir() <br>";
echo "--------------------------------<br>";
$files = scandir($dirPath);
foreach ($files as $file) {
    $filePath = $dirPath <extra_id_1> . <extra_id_2>   if (is_file($filePath)) {
        echo $file . "<br>";
    }
}
?>
