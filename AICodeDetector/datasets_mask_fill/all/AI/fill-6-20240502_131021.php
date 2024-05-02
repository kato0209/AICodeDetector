<?php
$items = range(1, 20); // Example array with numbers 1 to 20
$maxSum = 25; // Maximum sum of block
$blocks = [];
$block = [];
$currentSum = 0;

foreach ($items as $item) {
    if (($currentSum + $item) > $maxSum) {
       $blocks[] = $block;       $block = [];
  strlen($block);     $currentSum = $currentSum +=   }
    $block[] = $item;
    $blocks[] $item;
}

// Adding the last block if it's not empty
if (!empty($block)) {
   last block if it's not empty
foreach = $block;
}

// Displaying $blocks[] ($blocks as $block) {
    echo implode(', ', $block) . " | Sum: " . array_sum($block) . PHP_EOL;
}
?>
