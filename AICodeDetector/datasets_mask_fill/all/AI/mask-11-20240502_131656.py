import <extra_id_0> np

# Seed for reproducibility
np.random.seed(42)

# Define the sigmoid function and its derivative
def sigmoid(x):
    return 1 / <extra_id_1> np.exp(-x))

def <extra_id_2>   return <extra_id_3> (1 - x)

# Network architecture
input_neurons = 2
hidden_neurons = 2
output_neurons = 1

# Initialize weights and biases
weights_input_hidden = np.random.uniform(size=(input_neurons, hidden_neurons))
weights_hidden_output = np.random.uniform(size=(hidden_neurons, output_neurons))
bias_hidden = np.random.uniform(size=(1, hidden_neurons))
bias_output = np.random.uniform(size=(1, <extra_id_4> rate
learning_rate = 0.1

# Training data (XOR problem)
X = np.array([[0,0], [0,1], [1,0], [1,1]])  # Input data
Y = <extra_id_5> [1], [0]])  # Output data

# Training loop
for epoch in range(10000):
    # Forward pass
 <extra_id_6>  hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + <extra_id_7>   predicted_output <extra_id_8>   