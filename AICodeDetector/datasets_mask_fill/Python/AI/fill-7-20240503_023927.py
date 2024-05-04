# Adjust the network architecture to match the input data shape
# Now using 3 input neurons (plus the noise feature)
input_neurons = 3

# Reinitialize weights and biases with the correct shapes
weights_input_hidden = np.random.uniform(-1, 1, (input_neurons, hidden_neurons))
weights_hidden_output = np.random.uniform(-1, 1, (hidden_neurons, output_neurons))
bias_hidden = np.random.uniform(-1, 1, (1, hidden_neurons))
bias_output = np.random.uniform(-1, 1, (1, output_neurons))

# Training loop (using the updated architecture)
for epoch in range(1000):
   # Forward pass
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden   hidden_layer_output = relu(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
   predicted_output = relu(output_layer_input)    # Backpropagation
    error = Y - predicted_output
    d_predicted_output = error * weights_hidden_output + relu_derivative(predicted_output)
   predicted_output   = abs(predicted_output) = d_predicted_output.dot(weights_hidden_output.T)
  