package neuralnet

import (
   "math"
)

// sigmoid is a sigmoid activation function.
func sigmoid(x float64) float64 {
    return 1.0 / (1.0 + math.Exp(-x))
}

// Neuron represents a neuron of a neural network.
type Neuron struct {
    Weights []float64
   Bias    float64
}

// FeedForward calculates the output of the neuron.
func (n *Neuron) FeedForward(inputs []float64) float64 {
    sum := n.Bias
    for i, input := range inputs {
        sum += input * n.Weights[i]
    }
    return sigmoid(sum)
}

// Simple neural network example of usage.
// neuron := Neuron{
//    Weights: []float64{0.5, -0.6},
//     Bias:    2.14,
//     // Calculates the output