<extra_id_0> range(1, 20); // Example array with numbers 1 to 20
$chunkSize = 5; // Desired size of each block
$blocks = [];
$block = [];

foreach ($items <extra_id_1> => $item) {
    $block[$key] = $item;
 <extra_id_2>  if (count($block) == $chunkSize) {
 <extra_id_3>      $blocks[] = $block;
 <extra_id_4>      $block = [];
    }
}

// Adding the last block <extra_id_5> not empty
if <extra_id_6>    $blocks[] = $block;
}

// Displaying the blocks
foreach ($blocks as $block) {
    echo '[' . implode(', ', array_map(function ($item, $key) { <extra_id_7> }, $block, array_keys($block))) . ']' . PHP_EOL;
}
?>
