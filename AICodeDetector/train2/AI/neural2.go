package main

import (
	"fmt"
	"math/rand"
	"time"
)

type Matrix [][]float64

// Sigmoid function
func Sigmoid(x float64) float64 {
	return 1.0 / (1.0 + math.Exp(-x))
}

// Apply a function to each element of the matrix
func ApplyFunction(f func(float64) float64, matrix Matrix) Matrix {
	result := make(Matrix, len(matrix))
	for i, row := range matrix {
		result[i] = make([]float64, len(row))
		for j, val := range row {
			result[i][j] = f(val)
		}
	}
	return result
}

// Dot product of two matrices
func Dot(m1, m2 Matrix) Matrix {
	if len(m1[0]) != len(m2) {
		panic("incompatible dimensions")
	}
	result := make(Matrix, len(m1))
	for i := range result {
		result[i] = make([]float64, len(m2[0]))
		for j := range result[i] {
			sum := 0.0
			for k := range m1[i] {
				sum += m1[i][k] * m2[k][j]
			}
			result[i][j] = sum
		}
	}
	return result
}

type NeuralNetwork struct {
	inputSize       int
	hiddenSize      int
	outputSize      int
	weightsInputHidden Matrix
	weightsHiddenOutput Matrix
}

func NewNeuralNetwork(inputSize, hiddenSize, outputSize int) *NeuralNetwork {
	rand.Seed(time.Now().UnixNano())
	nn := &NeuralNetwork{
		inputSize:  inputSize,
		hiddenSize: hiddenSize,
		outputSize: outputSize,
	}

	// Initialize weights with random values
	nn.weightsInputHidden = RandomMatrix(inputSize, hiddenSize)
	nn.weightsHiddenOutput = RandomMatrix(hiddenSize, outputSize)

	return nn
}

// RandomMatrix generates a matrix with random values
func RandomMatrix(rows, cols int) Matrix {
	matrix := make(Matrix, rows)
	for i := range matrix {
		matrix[i] = make([]float64, cols)
		for j := range matrix[i] {
			matrix[i][j] = rand.Float64()*2 - 1 // Random values between -1 and 1
		}
	}
	return matrix
}

func (nn *NeuralNetwork) Forward(input Matrix) Matrix {
	hiddenInputs := Dot(input, nn.weightsInputHidden)
	hiddenOutputs := ApplyFunction(Sigmoid, hiddenInputs)

	finalInputs := Dot(hiddenOutputs, nn.weightsHiddenOutput)
	finalOutputs := ApplyFunction(Sigmoid, finalInputs)

	return finalOutputs
}

func main() {
	nn := NewNeuralNetwork(3, 4, 2) // 3 inputs, 4 hidden neurons, 2 outputs

	// Example input
	input := Matrix{{0.5, 0.1, -0.2}}
	output := nn.Forward(input)

	fmt.Println("Network output:", output)
}
