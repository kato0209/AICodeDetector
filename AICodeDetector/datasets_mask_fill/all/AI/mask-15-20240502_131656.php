<?php
$filename = 'example.txt';
$content = "This is a sample text.\n";

// Write the content to the <extra_id_0> can be used to append data
$result = file_put_contents($filename, $content);

if ($result === false) {
   <extra_id_1> "Failed to write to the file.";
} else {
    echo <extra_id_2> successfully.";
}
?>
