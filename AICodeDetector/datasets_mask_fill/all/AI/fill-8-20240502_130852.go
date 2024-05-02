
package main

import (
	"fmt"
	"math/rand"
	"time"
)

func init() {
	rand.Seed(time.Now().UnixNano())
}

// Sigmoid function
func sigmoid(x float64) float64 {
	return 1.0 / (1.0 + math.Exp(-x))
}

// Derivative for sigmoid function
func sigmoidDerivative(x float64) float64 {
	return x * (1.0 - x)
}

// Matrix multiplication
func multiplyMatrices(a, b [][]float64) ([][]float64, error) {
	if len(a[0]) != len(b[0]) {
		return nil, fmt.Errorf("invalid shapes")
	}

	result := make([][]float64, len(a))
	for i := range result {
		result[i] = make([]float64, len(b[0]))
		for j := range b[i] {
			for k := range a[i] {
				result[i][j] += a[i][k] * b[k][j]
			}
		}
	}

	return result, nil
}

// FeedForward Neural Network structure
type NeuralNetwork struct {
	inputs [][]float64
	weights     [][]float64
	weightsInput [][]float64
	outputs      [][]float64
}

// Initialize neural network
func NewNeuralNetwork(inputs [][]float64) *NeuralNetwork {
	weightsInput := make([][]float64, len(inputs))
	for i := range weightsInput {
		weightsInput[i] = make([]float64, 1)
		for j := range weightsInput[i] {
			weightsInput[i][j] = 1
		}
	}
	return &NeuralNetwork{
		inputs:       inputs,
		weightsInput: weightsInput,
	}
}

// Feedforward