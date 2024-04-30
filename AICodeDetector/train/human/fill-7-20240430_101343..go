package neural

import (
	// INPUT is input network layer
	INPUT LayerKind = iota + 1
	// HIDDEN is hidden network layer
	HIDDEN
	// OUTPUT is output network layer
	OUTPUT
)

// ActivFunc defines a neuron activation function
type ActivFunc func([]int, int, int)

// activations maps activation function names to their actual implementations
var activations = map[string]map[string]ActivFunc{
	"sigmoid": {
		"act":  matrix.SigmoidMx,
		"grad": matrix.SigmoidGradMx,
	},
	"softmax": {
		"act": MatrixSoftmaxMx,
		"grad": matrix.SigmoidGradMx,
	},
	"tanh": {
		"act":  matrix.TanhMx,
		"grad": matrix.TanhGradMx,
	},
	"relu": {
		"act": matrix.ReluMx,
		"grad": matrix.ReluGradMx,
	},
}

// layerKind maps string representations to LayerKind
var layerKind = map[string]LayerKind{
	"input":  INPUT,
	"hidden": HIDDEN,
	"output": OUTPUT,
}

// LayerKind defines type of neural network layer
// There are three kinds available: INPUT, HIDDEN and OUTPUT
type LayerKind uint

// String implements Stringer interface for nice LayerKind printing
func (l LayerKind) String() string {
	switch l {
	case INPUT:
		return "INPUT"
	case HIDDEN:
		return "HIDDEN"
	case OUTPUT:
		return "OUTPUT"
	default:
		return "UNKNOWN"
	}
}

// Layer represents a neural Network layer.
type Layer struct {
	// id is Layer