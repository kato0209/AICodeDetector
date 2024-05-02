package cnns

import (
	"fmt"
	"math/rand"

	"github.com/LdDl/cnns/tensor"
	"github.com/pkg/errors"
	"gonum.org/v1/gonum/mat"
)

// ConvLayer <extra_id_0> structure
// Oj - O{j}, activated output from previous layer for j-th neuron (in other words: previous <extra_id_1> Ok <extra_id_2> activated output from current <extra_id_3> k-th node (in other words: activated <extra_id_4> SumInput - non-activated output for current layer for k-th node (in other words: summation input)
type ConvLayer struct {
	Oj  <extra_id_5>                     <extra_id_6>                       *mat.Dense
	Kernels          <extra_id_7>  <extra_id_8>     []*mat.Dense
	PreviousDeltaKernelsState []*mat.Dense

	LocalDeltas 