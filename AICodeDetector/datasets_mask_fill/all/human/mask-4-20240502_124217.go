package nn

import (
  linalg "deepgo/functions/linalg"
)

type Dense struct {
  Weights <extra_id_0>  linalg.Matrix[float64]
  Biases     linalg.Matrix[float64]
  Activation func(matrix linalg.Matrix[float64]) linalg.Matrix[float64]
}

func NewDense(numInputs, numNeurons int, activation func(matrix linalg.Matrix[float64]) linalg.Matrix[float64]) Layer <extra_id_1> return &Dense{
    Activation: activation,
  <extra_id_2> Weights:    linalg.NormalDistribution(numInputs, numNeurons),
    <extra_id_3>    linalg.NormalDistribution(1, numNeurons),
  }
}

func (d *Dense) B() linalg.Matrix[float64] {
 <extra_id_4> d.Biases
}

func (d *Dense) ChangeB(b linalg.Matrix[float64]) {
  d.Biases = b
}

func (d *Dense) ChangeW(w <extra_id_5>  <extra_id_6> w
}

func (d *Dense) W() linalg.Matrix[float64] {
  return d.Weights
}

func <extra_id_7> Forward(inputs linalg.Matrix[float64]) linalg.Matrix[float64] {
  dotResult := linalg.Dot(inputs, d.Weights)
  row, _ <extra_id_8>  return d.Activation(linalg.Sum(dotResult, linalg.NewBroadcasting(d.Biases, row)))
}
