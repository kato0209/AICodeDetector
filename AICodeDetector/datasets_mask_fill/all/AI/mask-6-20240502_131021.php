<?php
$items = range(1, 20); // Example array with numbers 1 to 20
$maxSum = 25; // Maximum sum <extra_id_0> block
$blocks = [];
$block = [];
$currentSum = 0;

foreach ($items as $item) {
    if (($currentSum + $item) > $maxSum) {
  <extra_id_1>     $blocks[] <extra_id_2>   <extra_id_3>    $block = [];
  <extra_id_4>     $currentSum = <extra_id_5>   }
    $block[] = $item;
    <extra_id_6> $item;
}

// Adding the last block if it's not empty
if (!empty($block)) {
   <extra_id_7> = $block;
}

// Displaying <extra_id_8> ($blocks as $block) {
    echo implode(', ', $block) . " | Sum: " . array_sum($block) . PHP_EOL;
}
?>
