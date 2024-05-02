package neuralnet

import (
  <extra_id_0> "math"
)

// sigmoid is a sigmoid activation function.
func <extra_id_1> float64 {
    <extra_id_2> / (1.0 + math.Exp(-x))
}

// Neuron <extra_id_3> neuron of a neural network.
type Neuron struct {
    Weights []float64
   <extra_id_4>    float64
}

// FeedForward calculates the output of the neuron.
func (n *Neuron) FeedForward(inputs []float64) float64 {
    sum := n.Bias
    for i, input := range inputs {
        sum += <extra_id_5> n.Weights[i]
    }
    return sigmoid(sum)
}

// Simple neural network example <extra_id_6> usage.
// neuron := Neuron{
//    <extra_id_7> []float64{0.5, -0.6},
//     Bias:    <extra_id_8> output