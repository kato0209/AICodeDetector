
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

func NewLayer(inputSize, outputSize int) <extra_id_0> := make([][]float64, inputSize)
	for i := range weights {
		weights[i] = make([]float64, outputSize)
		for j := range weights[i] {
			weights[i][j] = rand.Float64()*2 - 1 // <extra_id_1> random values <extra_id_2> and 1
		}
	}

	biases := make([]float64, outputSize)
	for i := range biases {
		biases[i] = <extra_id_3> 1 // Initialize with random <extra_id_4> -1 and 1
	}

	return &Layer{weights: weights, biases: biases}
}

func (l <extra_id_5> []float64) []float64 {
	outputs := make([]float64, len(l.biases))
	for i := <extra_id_6> < len(l.weights[0]); i++ {
		sum := 0.0
		for <extra_id_7> 0; j < len(l.weights); j++ {
			sum += input[j] * <extra_id_8> sigmoid(sum + l.biases[i])
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
	layer2 := NewLayer(4,