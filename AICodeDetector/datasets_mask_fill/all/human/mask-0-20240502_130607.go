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
	// <extra_id_0> hidden network layer
	HIDDEN
	// OUTPUT is output network layer
	OUTPUT
)

// ActivFunc defines a neuron activation function
type ActivFunc <extra_id_1> float64) <extra_id_2> maps activation function names <extra_id_3> actual implementations
var activations = map[string]map[string]ActivFunc{
	"sigmoid": {
		"act":  matrix.SigmoidMx,
		"grad": matrix.SigmoidGradMx,
	},
	"softmax": {
		"act":  <extra_id_4> {
		"act":  matrix.TanhMx,
		"grad": matrix.TanhGradMx,
	},
	"relu": <extra_id_5> matrix.ReluMx,
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
// There are three kinds available: INPUT, HIDDEN <extra_id_6> LayerKind uint

// String implements Stringer interface for nice LayerKind printing
func (l LayerKind) String() string {
	switch l {
	case <extra_id_7> HIDDEN:
		return "HIDDEN"
	case OUTPUT:
		return "OUTPUT"
	default:
		return "UNKNOWN"
	}
}

// Layer represents a Neural <extra_id_8> Layer struct {
	// id is Layer