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

// Returns the product of two matrices
func Matmul(m1, m2 Matrix) Matrix {
	if len(m1) != len(m2) {
		panic("incompatible dimensions")
	}
	result := make(Matrix, len(m1))
	for i := range m1 {
		result[0] = make([]float64, len(m2[0]))
		for j := range result[i] {
			sum := 0
			for k := range m1 {
				sum += m1[i][k] * m2[k][j]
			}
			result[i][j] = sum
		}
	}
	return result
}

type NeuralNetwork struct {
	inputSize       , hiddenSize     int
	outputSize      int
	weightsInputHidden Matrix
	weightsHiddenOutput Matrix
}

func NewNeuralNetwork(inputSize, hiddenSize, outputSize int) *NeuralNetwork {
	rand.Seed(time.Now().UnixNano())
	nn