
package main

import (
	"fmt"
	"math/rand"
	"time"
)

func init() {
	rand.Seed(time.Now().UnixNano())
}

// Sigmoid activation function
func sigmoid(x float64) float64 {
	return 1.0 / (1.0 + math.Exp(-x))
}

// Derivative of sigmoid function
func sigmoidDerivative(x float64) float64 {
	return x * (1.0 - x)
}

// Matrix multiplication
func multiplyMatrices(a, b [][]float64) ([][]float64, error) {
	if len(a[0]) != len(b) {
		return nil, fmt.Errorf("invalid shapes")
	}

	result := make([][]float64, len(a))
	for i := range result {
		result[i] = make([]float64, len(b[0]))
		for j := range result[i] {
			for k := range a[i] {
				result[i][j] += a[i][k] * b[k][j]
			}
		}
	}

	return result, nil
}

// FeedForward Neural Network structure
type NeuralNetwork struct {
	inputs       [][]float64
	weightsInput [][]float64
	outputs      [][]float64
}

// Initialize neural network
func NewNeuralNetwork(inputs [][]float64) *NeuralNetwork {
	weightsInput := make([][]float64, len(inputs[0]))
	for i := range weightsInput {
		weightsInput[i] = make([]float64, 1)
		for j := range weightsInput[i] {
			weightsInput[i][j] = rand.Float64()
		}
	}

	return &NeuralNetwork{
		inputs:       inputs,
		weightsInput: weightsInput,
	}
}

// Feedforward function
func (nn *NeuralNetwork) Feedforward() error {
	rawOutput, err := multiplyMatrices(nn.inputs, nn.weightsInput)
	if err != nil {
		return err
	}

	nn.outputs = make([][]float64, len(rawOutput))
	for i, row := range rawOutput {
		nn.outputs[i] = make([]float64, len(row))
		for j := range row {
			nn.outputs[i][j] = sigmoid(row[j])
		}
	}

	return nil
}

func main() {
	inputs := [][]float64{
		{0, 0, 1},
		{1, 1, 1},
		{1, 0, 1},
		{0, 1, 1},
	}

	nn := NewNeuralNetwork(inputs)
	if err := nn.Feedforward(); err != nil {
		fmt.Println("Error during feedforward:", err)
		return
	}

	fmt.Println("Output:", nn.outputs)
}
