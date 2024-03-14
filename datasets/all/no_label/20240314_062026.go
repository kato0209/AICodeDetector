
package main

import (
	"fmt"
	"gonum.org/v1/gonum/mat"
)

// Define the structure for a Graph Neural Network
type GNN struct {
	W *mat.Dense // Weight matrix
}

// NewGNN initializes a new Graph Neural Network with given dimensions
func NewGNN(inputDim, outputDim int) *GNN {
	// Initialize weight matrix with random values
	W := mat.NewDense(outputDim, inputDim, nil)
	return &GNN{W: W}
}

// Forward performs the forward pass of the GNN
func (g *GNN) Forward(X *mat.Dense) *mat.Dense {
	// Compute the forward pass: Y = XW^T
	var Y mat.Dense
	Y.Mul(X, g.W.T())
	return &Y
}

func main() {
	// Example usage
	inputDim := 4
	outputDim := 2

	// Initialize GNN
	gnn := NewGNN(inputDim, outputDim)

	// Example input (4 nodes with 4 features each)
	X := mat.NewDense(4, 4, []float64{
		1, 2, 3, 4,
		4, 3, 2, 1,
		1, 3, 2, 4,
		4, 2, 3, 1,
	})

	// Perform forward pass
	Y := gnn.Forward(X)

	// Print output
	fmt.Println("Output:")
	fmt.Println(mat.Formatted(Y))
}
