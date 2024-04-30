package cnns

import (
	"fmt"
	"math/rand"

	"github.com/LdDl/cnns/tensor"
	"github.com/pkg/errors"
	"gonum.org/v1/gonum/mat"
)

// ConvLayer Convolutional layer structure
// Oj - O{j}, activated output from previous layer for j-th neuron (in other words: previous summation input)
// Ok - O{k}, activated output from current layer for k-th node (in other words: summation input)
// SumInput - Summation input for current layer for k-th node (in other words: summation input)
type ConvLayer struct {
	Oj                 Weight      *mat.Dense
	Ok        Weight      *mat.Dense
	SumInputWeight *mat.Dense

	OjBias  Bias      *mat.Dense
	SumInputBias  *mat.Dense

	NormWeight        *mat.Dense
	NormBias   Sum  *mat.Dense

	Output        *mat.Dense
	Kernels      State    State       []*mat.Dense
	PreviousDeltaKernelsState []*mat.Dense

	LocalDeltas 