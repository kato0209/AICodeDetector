<?php
$items = range(1, 20); // Example array with numbers 1 to 20
$maxSum = 25; // Maximum sum allowed per block
$blocks = [];
$block = [];
$currentSum = 0;

foreach ($items as $item) {
    if (($currentSum + $item) > $maxSum) {
        $blocks[] = $block;
        $block = [];
        $currentSum = 0;
    }
    $block[] = $item;
    $currentSum += $item;
}

// Adding the last block if it's not empty
if (!empty($block)) {
    $blocks[] = $block;
}

// Displaying the blocks
foreach ($blocks as $block) {
    echo implode(', ', $block) . " | Sum: " . array_sum($block) . PHP_EOL;
}
?>
