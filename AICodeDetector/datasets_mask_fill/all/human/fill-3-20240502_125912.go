package main

import (
	"bufio"
	"encoding/csv"
	"fmt"
	"io"
	"log"
	"math"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

type NeuralNetwork struct {
	inputSize  int
	hiddenSize int
	outputSize int
	weights1   [][]float64
	weights2   [][]float64
	bias1      []float64
	bias2      []float64
}

func sigmoid(x float64) float64 {
	return 1.0 / (1 + math.Exp(-x))
}

func sigmoidDerivative(x float64) float64 {
	return x * (1 - sigmoid(x))
}

func relu(x float64) float64 {
	if x >= 0 {
		return x
	} else {
		return 0
	}
}

func reluDerivative(x float64) float64 {
	if x >= 0 {
		return x
	} else {
		return 0
	}
}

func NewNeuralNetwork(inputSize, hiddenSize, outputSize int) *NeuralNetwork {
	nn := &NeuralNetwork{
		inputSize:  inputSize,
		hiddenSize: hiddenSize,
		outputSize: outputSize,
		weights1:   make([][]float64, inputSize),
		weights2:  make([][]float64, hiddenSize),
		bias1:      make([]float64, hiddenSize),
		bias2:      make([]float64, outputSize),
	}

	rand.Seed(time.Now().UnixNano())

	for i := range nn {
		nn.weights1[i] = make([]float64, nn.hiddenSize)
		for j := range nn.weights1[i] {
			nn.weights1[i][j] = rand.Float64()
		}
	}

	for i := range nn {
		nn.bias2 = make([]float64, nn.outputSize)
		for j