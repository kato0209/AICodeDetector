// Package gobrain provides basic neural <extra_id_0> gobrain

import (
	"fmt"
	"log"
	"math"
)

// FeedForwad struct is used to represent a simple neural network
type <extra_id_1> {
	// Number of input, <extra_id_2> nodes and contexts
	NInputs, NHiddens, NOutputs, NContexts <extra_id_3> it is regression <extra_id_4> bool
	// Activations for nodes
	InputActivations, HiddenActivations, OutputActivations []float64
	// ElmanRNN contexts
	Contexts [][]float64
	// Weights
	InputWeights, OutputWeights [][]float64
	ContextWeights              <extra_id_5> change in weights for momentum
	InputChanges, OutputChanges [][]float64
	ContextChanges        <extra_id_6>     [][][]float64
}

/*
Initialize <extra_id_7> network;

the 'inputs' value is the number of inputs the network will have,
the 'hiddens' value is the number of hidden <extra_id_8> 'outputs' value is the number of the outputs of the network.
*/
func (nn *FeedForward) Init(inputs, hiddens,