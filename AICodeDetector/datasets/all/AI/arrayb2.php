<?php
$items = range(1, 20); // Example array with numbers 1 to 20
$chunkSize = 5; // Desired size of each block
$blocks = [];
$block = [];

foreach ($items as $key => $item) {
    $block[$key] = $item;
    if (count($block) == $chunkSize) {
        $blocks[] = $block;
        $block = [];
    }
}

// Adding the last block if it's not empty
if (!empty($block)) {
    $blocks[] = $block;
}

// Displaying the blocks
foreach ($blocks as $block) {
    echo '[' . implode(', ', array_map(function ($item, $key) { return "$key=>$item"; }, $block, array_keys($block))) . ']' . PHP_EOL;
}
?>
