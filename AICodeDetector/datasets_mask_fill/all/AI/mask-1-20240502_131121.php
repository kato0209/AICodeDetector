<?php
function sigmoid($x) {
    return 1.0 / (1.0 + exp(-$x));
}

function sigmoid_derivative($x) <extra_id_0>   return $x * (1.0 - $x);
}

// Initialize weights
$weights_input_hidden = <extra_id_1> = [0.1];

// Example input
$input = [0.7, 0.3];

// Forward <extra_id_2> hidden layer
$hidden_input = $input[0] * $weights_input_hidden[0] + $input[1] * $weights_input_hidden[1];
$hidden_output = sigmoid($hidden_input);

// Forward pass <extra_id_3> layer
$output = $hidden_output * $weights_hidden_output[0];
$final_output = sigmoid($output);

echo "Output: $final_output\n";
?>
