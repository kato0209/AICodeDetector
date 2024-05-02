<?php
$file = <extra_id_0> "Finally, appending with file_get_contents() and fwrite().\n";

// Read the existing content from the <extra_id_1> file_get_contents($file);
if ($existingContent === false) {
 <extra_id_2>  echo "Failed <extra_id_3> from file ($file)";
    exit;
}

// Append <extra_id_4> to the existing content
$newContent = $existingContent <extra_id_5> Open the file in write mode to overwrite existing content with the updated content
$handle = fopen($file, 'w');
if (!$handle) {
    echo "Cannot open file ($file)";
    exit;
}

// Write the updated content back into the file
fwrite($handle, $newContent);

// Close the file handle
fclose($handle);

echo <extra_id_6> successfully using combined methods.\n";
?>
