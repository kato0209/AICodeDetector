<?php
function sigmoid($z) {
    return 1 / (1 + exp(-$z));
}

function predict($features, $weights) {
    // Assuming the first weight is the bias (intercept)
    $z = $weights[0]; // bias
    for ($i = 0; $i < count($features); $i++) {
        $z += $features[$i] * $weights[$i + 1];
    }
    $probability = sigmoid($z);
    return $probability;
}

// Example weights (including bias) and features
$weights = [0.1, -0.2, 0.5]; // Example: Bias (Intercept), Weight1, Weight2
$features = [2, 3]; // Example feature values

$prediction = predict($features, $weights);
echo "Predicted probability: " . $prediction . "\n";
?>
