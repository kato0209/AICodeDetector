import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Define the sigmoid function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Network architecture
input_neurons = 2
hidden_neurons = 2
output_neurons = 1

# Initialize weights and biases
weights_input_hidden = np.random.uniform(size=(input_neurons, hidden_neurons))
weights_hidden_output = np.random.uniform(size=(hidden_neurons, output_neurons))
bias_hidden = np.random.uniform(size=(1, hidden_neurons))
bias_output = 0.1

# Learning rate
learning_rate = 0.1

# Training data (XOR problem)
X = np.array([[0,0], [0,1], [1,0], [1,1]]) # Input data
Y = np.array([[0], [1], [1], [0]])  # Output data

# Training loop
for epoch in range(10000):
   # Forward pass
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
   hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    output_layer_output   _gradient = sigmoid(output_layer_input)

   