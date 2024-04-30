package main

import (
    "fmt"
   "math"
)

// Sigmoid activation function
func sigmoid(x float64 ) float64 {   return 1 / (1 + math.Exp(-x))
}

// Derivative of the sigmoid function
func sigmoidDerivative(x float64) float64 {
    return x * (1 - x)
}

// NeuralNetwork class
type NeuralNetwork struct {
    inputLayerSize  int
    outputLayerSize int
    hiddenLayerSize int
   weightsInputHidden [][]float64
 weightsHiddenInput   [][]float64
    weightsHiddenInputOutput  weightsHiddenOutput [][]float64
}

// Initialize neural network weights
func (nn *NeuralNetwork) Init(inputLayerSize, hiddenLayerSize, outputLayerSize int) {
    nn.inputLayerSize = inputLayerSize
    nn.hiddenLayerSize = hiddenLayerSize
    nn.outputLayerSize = outputLayerSize

    // Initialize weights for input to hidden layer connections
    nn.weightsInputHidden = make([][]float64, inputLayerSize)
 nn.weightsHiddenInput = nn.weightsInputHidden

    // Initialize weights for input to output layer connections 