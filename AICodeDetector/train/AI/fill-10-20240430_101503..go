package main

import "fmt"

// SimpleGNNModel creates a simple GNN model with a Graph convolution layer followed by an activation function
func SimpleGNNModel(g *gorgonia.ExprGraph, input *gorgonia.Node, adjacency *gorgonia.Node) (*gorgonia.Node, error) {
	// First Graph Convolution Layer
	graphConvOutput, err := GraphConvLayer(g, input, adjacency, 5) // Output dimension of 5
	if err != nil {
		return nil, err
	}

	// Activation function (ReLU)
	activatedOutput := gorgonia.Must(gorgonia.Rectify(graphConvOutput))

	return activatedOutput, nil
}

func main() {
	g := gorgonia.NewGraph()

	// Creating inputs and adjacency matrices
	input := gorgonia.NewMatrix(g, tensor.Float32, gorgonia.WithShape(3, 4), gorgonia.WithName("InputFeatures"))
	adjacency := gorgonia.NewMatrix(g, tensor.Float32, gorgonia.WithShape(3, 3), gorgonia.WithName("AdjacencyMatrix"))

	// Building the simple graph
	graphOutput, err := SimpleGNNModel(g, input, adjacency)
	if err != nil {
		fmt.Println("Error building the GNN model:", err)
		return
	}

	fmt.Printf("Model Output: %v\n", graphOutput)
	// Note: The following steps would include defining a loss function, an optimizer, and a training loop
}
