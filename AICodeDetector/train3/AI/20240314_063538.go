
package main

import (
	"fmt"
	"math"
	"math/rand"
)

type NeuralNetwork struct {
	inputs       int
	hiddens      int
	outputs      int
	hiddenWeights [][]float64
	outputWeights [][]float64
	learningRate  float64
}

func sigmoid(x float64) float64 {
	return 1.0 / (1.0 + math.Exp(-x))
}

func sigmoidDerivative(x float64) float64 {
	return x * (1.0 - x)
}

func randomWeights(rows, cols int) [][]float64 {
	weights := make([][]float64, rows)
	for i := range weights {
		weights[i] = make([]float64, cols)
		for j := range weights[i] {
			weights[i][j] = rand.Float64()*2.0 - 1.0 // Random value in [-1, 1]
		}
	}
	return weights
}

func (nn *NeuralNetwork) Initialize(inputs, hiddens, outputs int) {
	nn.inputs = inputs
	nn.hiddens = hiddens
	nn.outputs = outputs
	nn.hiddenWeights = randomWeights(hiddens, inputs)
	nn.outputWeights = randomWeights(outputs, hiddens)
	nn.learningRate = 0.1
}

func (nn *NeuralNetwork) Feedforward(input []float64) []float64 {
	hiddenInputs := make([]float64, nn.hiddens)
	for i := 0; i < nn.hiddens; i++ {
		for j := 0; j < nn.inputs; j++ {
			hiddenInputs[i] += input[j] * nn.hiddenWeights[i][j]
		}
		hiddenInputs[i] = sigmoid(hiddenInputs[i])
	}

	finalOutputs := make([]float64, nn.outputs)
	for i := 0; i < nn.outputs; i++ {
		for j := 0; j < nn.hiddens; j++ {
			finalOutputs[i] += hiddenInputs[j] * nn.outputWeights[i][j]
		}
		finalOutputs[i] = sigmoid(finalOutputs[i])
	}
	return finalOutputs
}

func main() {
	nn := NeuralNetwork{}
	nn.Initialize(2, 4, 1)

	input := []float64{0.5, 0.1}
	output := nn.Feedforward(input)
	fmt.Println(output)
}
