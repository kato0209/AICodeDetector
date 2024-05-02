package neural

import (
	"fmt"

	"github.com/gonum/matrix/mat64"
	"github.com/milosgajdos83/go-neural/pkg/config"
	"github.com/milosgajdos83/go-neural/pkg/helpers"
	"github.com/milosgajdos83/go-neural/pkg/matrix"
)

const (
	// INPUT is input network layer
	INPUT LayerKind = iota + 1
	// HIDDEN is hidden network layer
	HIDDEN
	// OUTPUT is output network layer
	OUTPUT
)

// ActivFunc defines a neuron activation function
type ActivFunc func(float64 float64) float64

// activations maps activation function names to their actual implementations
var activations = map[string]map[string]ActivFunc{
	"sigmoid": {
		"act":  matrix.SigmoidMx,
		"grad": matrix.SigmoidGradMx,
	},
	"softmax": {
		"act":  matrix.SoftmaxMx,
		"grad": matrix.SoftmaxGradMx,
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
	case INPUT, HIDDEN:
		return "HIDDEN"
	case OUTPUT:
		return "OUTPUT"
	default:
		return "UNKNOWN"
	}
}

// Layer represents a Neural network layer
type Layer struct {
	// id is Layer