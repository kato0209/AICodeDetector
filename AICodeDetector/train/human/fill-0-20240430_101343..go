package neural

import (
	"fmt"

	"github.com/gonum/matrix/mat64"
	"github.com/gonum/optimize"
	"github.com/milosgajdos83/go-neural/pkg/config"
	"github.com/milosgajdos83/go-neural/pkg/helpers"
	"github.com/milosgajdos83/go-neural/pkg/matrix"
)

const (
	// FEEDFWD is a feed forward Neural Network
	FEEDFWD NetworkKind = iota + 1
)

// optim maps optimization algorithm names to their constructor
var optim = map[string]optimize.Method{
	"bfgs": &optimize.BFGS{},
}

// kindMap maps strings to NetworkKind
var netKind = map[string]NetworkKind{
	"feedfwd": FEEDFWD,
}

// This type defines a type of neural network
type NetworkKind uint

// String implements Stringer interface for pretty printing
func (n NetworkKind) String() string {
	switch n {
	case FEEDFWD:
		return "FEEDFWD"
	default:
		return "UNKNOWN"
	}
}

// network maps supported neural network types to their constructors
var network = map[string]func(*config.NetArch) (*Network, error){
	"feedfwd": createFeedFwdNetwork,
}

// The Neural Network contains the neural network parameters to
// be constructed.
type NeuralNetwork struct {
	id     string
	kind  NetworkKind
	layers LayerList
}

// Create creates new Neural Network based on the provided configuration parameters.
// It fails with error if either the requested network type is not supported or
// if any of the neural network layers