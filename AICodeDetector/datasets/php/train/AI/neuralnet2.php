<?php
function sigmoid($x) {
    return 1.0 / (1.0 + exp(-$x));
}

function sigmoid_derivative($x) {
    return $x * (1.0 - $x);
}

// Initialize weights
$weights_input_hidden = [[0.5, -0.6], [0.4, -0.7]];
$weights_hidden_output = [0.1, -0.2];

// Initialize biases
$bias_hidden = [0.1];
$bias_output = -0.2;

// Example input
$input = [0.7, 0.3];

// Forward pass to hidden layer
$hidden_input = [$input[0] * $weights_input_hidden[0][0] + $input[1] * $weights_input_hidden[0][1] + $bias_hidden[0],
                 $input[0] * $weights_input_hidden[1][0] + $input[1] * $weights_input_hidden[1][1] + $bias_hidden[0]];
$hidden_output = array_map('sigmoid', $hidden_input);

// Forward pass to output layer
$output = $hidden_output[0] * $weights_hidden_output[0] + $hidden_output[1] * $weights_hidden_output[1] + $bias_output;
$final_output = sigmoid($output);

echo "Output: $final_output\n";
?>
