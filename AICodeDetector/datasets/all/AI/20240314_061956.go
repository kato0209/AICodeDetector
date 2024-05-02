
package main

import (
	"fmt"
	"math/rand"
	"time"
)

// Activation function
func sigmoid(x float64) float64 {
	return 1.0 / (1.0 + math.Exp(-x))
}

// Derivative of the activation function
func sigmoidPrime(x float64) float64 {
	return sigmoid(x) * (1.0 - sigmoid(x))
}

// Matrix struct
type Matrix struct {
	rows, cols int
	data       [][]float64
}

// NewMatrix creates a new matrix
func NewMatrix(rows, cols int) *Matrix {
	m := &Matrix{
		rows: rows,
		cols: cols,
		data: make([][]float64, rows),
	}
	for i := range m.data {
		m.data[i] = make([]float64, cols)
	}
	return m
}

// Apply a function to each element of the matrix
func (m *Matrix) mapFunc(f func(float64) float64) {
	for i := range m.data {
		for j := range m.data[i] {
			m.data[i][j] = f(m.data[i][j])
		}
	}
}

// NeuralNetwork struct
type NeuralNetwork struct {
	inputNodes  int
	hiddenNodes int
	outputNodes int
	weightsIH   *Matrix
	weightsHO   *Matrix
	biasH       *Matrix
	biasO       *Matrix
	learningRate float64
}

// NewNeuralNetwork creates a new Neural Network
func NewNeuralNetwork(inputNodes, hiddenNodes, outputNodes int) *NeuralNetwork {
	rand.Seed(time.Now().UnixNano())

	nn := &NeuralNetwork{
		inputNodes:  inputNodes,
		hiddenNodes: hiddenNodes,
		outputNodes: outputNodes,
		weightsIH:   NewMatrix(hiddenNodes, inputNodes),
		weightsHO:   NewMatrix(outputNodes, hiddenNodes),
		biasH:       NewMatrix(hiddenNodes, 1),
		biasO:       NewMatrix(outputNodes, 1),
		learningRate: 0.1,
	}

	// Randomly initialize weights and biases
	for i := 0; i < hiddenNodes; i++ {
		for j := 0; j < inputNodes; j++ {
			nn.weightsIH.data[i][j] = rand.NormFloat64() * 0.1
		}
		nn.biasH.data[i][0] = rand.NormFloat64() * 0.1
	}

	for i := 0; i < outputNodes; i++ {
		for j := 0; j < hiddenNodes; j++ {
			nn.weightsHO.data[i][j] = rand.NormFloat64() * 0.1
		}
		nn.biasO.data[i][0] = rand.NormFloat64() * 0.1
	}

	return nn
}

func main() {
	// Example usage
	inputNodes := 2
	hiddenNodes := 4
	outputNodes := 1

	nn := NewNeuralNetwork(inputNodes, hiddenNodes, outputNodes)

	fmt.Println("Neural Network created with", inputNodes, "input nodes,", hiddenNodes, "hidden nodes, and", outputNodes, "output nodes.")
}
