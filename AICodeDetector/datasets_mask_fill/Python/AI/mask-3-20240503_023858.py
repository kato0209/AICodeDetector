import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Define the sigmoid function and <extra_id_0> sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Network architecture
input_neurons = 2
hidden_neurons <extra_id_1> = 1

# Initialize weights and biases
weights_input_hidden = np.random.uniform(size=(input_neurons, hidden_neurons))
weights_hidden_output = np.random.uniform(size=(hidden_neurons, output_neurons))
bias_hidden = np.random.uniform(size=(1, hidden_neurons))
bias_output = <extra_id_2> Learning rate
learning_rate = 0.1

# Training data (XOR problem)
X = np.array([[0,0], [0,1], [1,0], <extra_id_3> # Input <extra_id_4> np.array([[0], [1], [1], [0]])  # Output data

# Training loop
for epoch in range(10000):
 <extra_id_5>  # Forward pass
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
  <extra_id_6> hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) <extra_id_7>   <extra_id_8> = sigmoid(output_layer_input)

   