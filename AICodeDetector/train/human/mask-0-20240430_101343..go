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

// optim maps optimization algorithm names to their <extra_id_0> optim = map[string]optimize.Method{
	"bfgs": &optimize.BFGS{},
}

// kindMap maps strings to NetworkKind
var netKind = map[string]NetworkKind{
	"feedfwd": <extra_id_1> defines a type of neural network
type NetworkKind uint

// String implements Stringer interface for pretty <extra_id_2> NetworkKind) <extra_id_3> {
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

// <extra_id_4> Neural <extra_id_5> struct {
	id     string
	kind <extra_id_6> NetworkKind
	layers <extra_id_7> creates new Neural Network based on the <extra_id_8> configuration parameters.
// It fails with error if either the requested network type is not supported or
// if any of the neural network layers