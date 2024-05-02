
package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

type Layer struct {
	weights [][]float64
	biases  []float64
	output  []float64
}

func NewLayer(inputSize, outputSize int) *Layer {
	rand.Seed(time.Now().UnixNano())
	weights := make([][]float64, inputSize)
	for i := range weights {
		weights[i] = make([]float64, outputSize)
		for j := range weights[i] {
			weights[i][j] = rand.Float64()*2 - 1 // Initialize with random values between -1 and 1
		}
	}

	biases := make([]float64, outputSize)
	for i := range biases {
		biases[i] = rand.Float64()*2 - 1 // Initialize with random values between -1 and 1
	}

	return &Layer{weights: weights, biases: biases}
}

func (l *Layer) Forward(input []float64) []float64 {
	outputs := make([]float64, len(l.biases))
	for i := 0; i < len(l.weights[0]); i++ {
		sum := 0.0
		for j := 0; j < len(l.weights); j++ {
			sum += input[j] * l.weights[j][i]
		}
		outputs[i] = sigmoid(sum + l.biases[i])
	}
	l.output = outputs
	return outputs
}

func sigmoid(x float64) float64 {
	return 1 / (1 + math.Exp(-x))
}

func main() {
	input := []float64{0.5, -0.1, 0.3}
	layer1 := NewLayer(3, 4)
	layer2 := NewLayer(4, 2)

	outputFromLayer1 := layer1.Forward(input)
	finalOutput := layer2.Forward(outputFromLayer1)

	fmt.Println(finalOutput)
}
