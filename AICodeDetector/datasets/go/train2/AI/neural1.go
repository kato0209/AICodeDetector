package main

import (
    "fmt"
    "math"
)

// Sigmoid activation function
func sigmoid(x float64) float64 {
    return 1 / (1 + math.Exp(-x))
}

// Derivative of the sigmoid function
func sigmoidDerivative(x float64) float64 {
    return x * (1 - x)
}

// NeuralNetwork structure
type NeuralNetwork struct {
    inputLayerSize  int
    outputLayerSize int
    hiddenLayerSize int
    weightsInputHidden [][]float64
    weightsHiddenOutput [][]float64
}

// Initialize neural network weights
func (nn *NeuralNetwork) Init(inputLayerSize, hiddenLayerSize, outputLayerSize int) {
    nn.inputLayerSize = inputLayerSize
    nn.hiddenLayerSize = hiddenLayerSize
    nn.outputLayerSize = outputLayerSize

    // Initialize weights for the input to hidden layer connections
    nn.weightsInputHidden = make([][]float64, inputLayerSize)
    for i := range nn.weightsInputHidden {
        nn.weightsInputHidden[i] = make([]float64, hiddenLayerSize)
        for j := range nn.weightsInputHidden[i] {
            nn.weightsInputHidden[i][j] = 0.5 // Simplified initialization
        }
    }

    // Initialize weights for the hidden to output layer connections
    nn.weightsHiddenOutput = make([][]float64, hiddenLayerSize)
    for i := range nn.weightsHiddenOutput {
        nn.weightsHiddenOutput[i] = make([]float64, outputLayerSize)
        for j := range nn.weightsHiddenOutput[i] {
            nn.weightsHiddenOutput[i][j] = -0.5 // Simplified initialization
        }
    }
}

// Forward propagation
func (nn *NeuralNetwork) Forward(input []float64) []float64 {
    hiddenLayerInputs := make([]float64, nn.hiddenLayerSize)
    for i := 0; i < nn.hiddenLayerSize; i++ {
        sum := 0.0
        for j := 0; j < nn.inputLayerSize; j++ {
            sum += input[j] * nn.weightsInputHidden[j][i]
        }
        hiddenLayerInputs[i] = sigmoid(sum)
    }

    outputLayerInputs := make([]float64, nn.outputLayerSize)
    for i := 0; i < nn.outputLayerSize; i++ {
        sum := 0.0
        for j := 0; j < nn.hiddenLayerSize; j++ {
            sum += hiddenLayerInputs[j] * nn.weightsHiddenOutput[j][i]
        }
        outputLayerInputs[i] = sigmoid(sum)
    }

    return outputLayerInputs
}

func main() {
    nn := NeuralNetwork{}
    nn.Init(3, 4, 1) // Example sizes: 3 input neurons, 4 hidden neurons, 1 output neuron

    input := []float64{1.0, 0.5, -1.0}
    output := nn.Forward(input)

    fmt.Println("Output:", output)
}
