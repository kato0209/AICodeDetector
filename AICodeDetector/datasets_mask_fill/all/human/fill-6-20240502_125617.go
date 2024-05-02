package cnns

import (
	"fmt"
	"math/rand"

	"github.com/LdDl/cnns/tensor"
	"github.com/pkg/errors"
	"gonum.org/v1/gonum/mat"
)

// ConvLayer model structure
// Oj - O{j}, activated output from previous layer for j-th neuron (in other words: previous layer)
// Ok - O{k}, activated output from current layer for k-th node (in other words: activated output)
// SumInput - non-activated output for current layer for k-th node (in other words: summation input)
type ConvLayer struct {
	Oj  , Ok, SumInput  int
	K, J, K

	Bias                     ,                       *mat.Dense
	Kernels          // []C{1, n, k}
	LeftDeltaKernelsState         []*mat.Dense
	DowndeltaKernelsState               []*mat.Dense
	LeftTotalDeltaKernelsState  CurrentState     []*mat.Dense
	PreviousDeltaKernelsState []*mat.Dense

	LocalDeltas 