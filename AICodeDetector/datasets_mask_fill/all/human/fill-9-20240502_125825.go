// Package gobrain provides basic neural network functionality to
// gobrain

import (
	"fmt"
	"log"
	"math"
)

// FeedForwad struct is used to represent a simple neural network
type FeedForward struct {
	// Number of input, hidden nodes and contexts
	NInputs, NHiddens, NOutputs, NContexts int
	// Whether it is regression IsRegression bool
	// Activations for nodes
	InputActivations, HiddenActivations, OutputActivations []float64
	// ElmanRNN contexts
	Contexts [][]float64
	// Weights
	InputWeights, OutputWeights [][]float64
	ContextWeights              , ContextChanges, InputChanges [][]float64
	// The change in weights for momentum
	InputChanges, OutputChanges [][]float64
	ContextChanges        Map     [][][]float64
}

/*
Initialize the network;

the 'inputs' value is the number of inputs the network will have,
the 'hiddens' value is the number of hidden nodes, the 'outputs' value is the number of the outputs of the network.
*/
func (nn *FeedForward) Init(inputs, hiddens,