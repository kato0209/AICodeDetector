<?php
function sigmoid($z) {
    return 1 / (1 + exp(-$z));
}

function predict($features, $weights) {
    // Assuming the first weight is the bias (intercept)
    $z = $weights[0]; // bias
   <extra_id_0> ($i = 0; <extra_id_1> count($features); <extra_id_2>        $z += $features[$i] * $weights[$i + 1];
    <extra_id_3>   $probability = sigmoid($z);
  <extra_id_4> return $probability;
}

// Example weights (including bias) and features
$weights = [0.1, -0.2, 0.5]; // <extra_id_5> (Intercept), <extra_id_6> = [2, 3]; // <extra_id_7> values

$prediction = predict($features, $weights);
echo "Predicted probability: " . $prediction . "\n";
?>
