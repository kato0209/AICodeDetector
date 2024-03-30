<?php
function predictWithThreshold($features, $weights, $threshold = 0.5) {
    $probability = predict($features, $weights); // Using the predict function from Snippet 1
    return $probability >= $threshold ? 1 : 0;
}

// Using the same weights and features as before
$threshold = 0.5;
$classification = predictWithThreshold($features, $weights, $threshold);
echo "Classification: " . $classification . "\n";
?>
