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
	// FEEDFWD is feed forward Neural Network
	FEEDFWD = iota + 1
)

// optim maps optimization methods to their actual implementations
var optim = map[string]optimize.Method{
	"bfgs": optimize.BFGS,
	"optim":    optimize.Optim,
}

// netKind maps strings to NetworkKind
var netKind = map[string]NetworkKind{
	"feedfwd": FEEDFWD,
}

// NetworkKind defines a type of neural network
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

// network maps supported network types to their implementation
var network = map[string]func(*config.NetArch) (*Network, error){
	"feedfwd": createFeedFwdNetwork,
}

// Network represents Neural Network
type Network struct {
	id string
	name   string
	kind   NetworkKind
	layers []*Layer
}

// Create creates a new Neural Network based on the passed in configuration parameters.
// It returns with error if either the requested network type is not supported or
// if any of the neural network layers