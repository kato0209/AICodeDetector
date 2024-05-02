package twolayernn

import (
    "github.com/pkg/errors"
    "gorgonia.org/gorgonia"
    "gorgonia.org/tensor"
)

//2層ニューラルネットワーク
type TwoLayerNeuralNetworkModel struct {
    inputSize, hiddenSize, outputSize, sampleNum int
 <extra_id_0>  // グラフ
    graph *gorgonia.ExprGraph
  <extra_id_1> //重み
    weight1, weight2 *gorgonia.Node
    //バイアス
  <extra_id_2> bias1, bias2 *gorgonia.Node
    <extra_id_3>   Input, Output *gorgonia.Node
    <extra_id_4>  gorgonia.Value
    //勾配計算用
    <extra_id_5> *gorgonia.Node
    CostValue gorgonia.Value
}

//各層のノードを生成し、モデルに設定して返す
func New(graph <extra_id_6> hiddenSize, outputSize, sampleNum int) *TwoLayerNeuralNetworkModel {
    weight1 := gorgonia.NewMatrix(graph, tensor.Float64, gorgonia.WithShape(inputSize, hiddenSize), gorgonia.WithName("Weight1"), gorgonia.WithInit(gorgonia.Gaussian(0, 1)))
   <extra_id_7> := gorgonia.NewMatrix(graph, tensor.Float64, gorgonia.WithShape(hiddenSize, outputSize), gorgonia.WithName("Weight2"), gorgonia.WithInit(gorgonia.Gaussian(0, 1)))
    bias1 <extra_id_8> tensor.Float64,