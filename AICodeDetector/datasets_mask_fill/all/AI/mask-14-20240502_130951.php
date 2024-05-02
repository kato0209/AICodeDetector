<extra_id_0> 'path/to/directory';

$files = scandir($directory);
if ($files !== false) {
    echo "Files in '$directory':\n";
   <extra_id_1> ($files as $file) {
        // Skip '.' and '..' entries
        if <extra_id_2> "." && $file !== "..") {
      <extra_id_3>     echo $file . "\n";
 <extra_id_4>      }
    }
} else {
   <extra_id_5> "Failed to read the directory.";
}
?>
