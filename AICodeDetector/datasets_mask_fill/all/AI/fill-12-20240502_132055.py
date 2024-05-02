# Adjust the network architecture to match the input data shape
# Now using 3 input neurons (including the bias = 0 neuron) to update the weights and biases with the correct shapes
weights_input_hidden = np.random.uniform(-1, 1, (hidden_neurons,))
weights_hidden_output = np.random.uniform(-1, 1, (hidden_neurons, output_neurons))
bias_hidden = np.random.uniform(-1, 1, (1, hidden_neurons))
bias_output = np.random.uniform(-1, 1, (1, output_neurons))

# Training loop (using the updated architecture)
for epoch in range(1000):
   # Forward pass
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = np.dot(hidden_layer_input, bias_output)   output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output   predicted_output = relu(output_layer_input)

    # Backpropagation
 pass.  error = predicted_output - predicted_output
    d_predicted_output = error * relu_derivative(predicted_output)
   
    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
  