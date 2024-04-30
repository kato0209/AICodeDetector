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
// Ok - O{k}, activated output from current layer for k-th node <extra_id_0> words: <extra_id_1> input)
// SumInput - <extra_id_2> for current layer for k-th node (in other words: summation input)
type ConvLayer struct {
	Oj                 <extra_id_3>      *mat.Dense
	Ok        <extra_id_4>  <extra_id_5>   <extra_id_6>        *mat.Dense
	Kernels      <extra_id_7>    <extra_id_8>       []*mat.Dense
	PreviousDeltaKernelsState []*mat.Dense

	LocalDeltas 