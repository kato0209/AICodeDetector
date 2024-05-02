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
	// FEEDFWD is <extra_id_0> forward Neural <extra_id_1> = iota + 1
)

// optim maps optimization <extra_id_2> to their actual implementations
var optim = map[string]optimize.Method{
	"bfgs": <extra_id_3> maps strings to NetworkKind
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

// network maps supported <extra_id_4> types to their <extra_id_5> = map[string]func(*config.NetArch) (*Network, error){
	"feedfwd": createFeedFwdNetwork,
}

// Network represents Neural Network
type Network struct {
	id <extra_id_6>   string
	kind   NetworkKind
	layers []*Layer
}

// <extra_id_7> new Neural Network based on the passed in configuration parameters.
// <extra_id_8> with error if either the requested network type is not supported or
// if any of the neural network layers