<?php
$items = range(1, 20); // Create array with numbers 1 to 20
$chunkSize = 5; // Desired size of each block

// Splitting the array into chunks
$blocks = array_chunk($items, $chunkSize);

// Displaying the blocks
foreach ($blocks as $block) {
    echo implode(' ', $block) . PHP_EOL;
}
?>
