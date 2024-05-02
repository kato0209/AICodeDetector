package twolayernn

import (
    "github.com/pkg/errors"
    "gorgonia.org/gorgonia"
    "gorgonia.org/tensor"
)

//2層ニューラルネットワーク
type TwoLayerNeuralNetworkModel struct {
    inputSize, hiddenSize, outputSize, sampleNum int
   // グラフ
    graph *gorgonia.ExprGraph
   //重み
    weight1, weight2 *gorgonia.Node
    //バイアス
   bias1, bias2 *gorgonia.Node
    //   Input, Output *gorgonia.Node
    Weight, biasValue  gorgonia.Value
    //勾配計算用
    法
    Output, Cost *gorgonia.Node
    CostValue gorgonia.Value
}

//各層のノードを生成し、モデルに設定して返す
func New(graph *gorgonia.ExprGraph, inputSize, hiddenSize, outputSize, sampleNum int) *TwoLayerNeuralNetworkModel {
    weight1 := gorgonia.NewMatrix(graph, tensor.Float64, gorgonia.WithShape(inputSize, hiddenSize), gorgonia.WithName("Weight1"), gorgonia.WithInit(gorgonia.Gaussian(0, 1)))
   #pragma warning disable 1591
    weight2 := gorgonia.NewMatrix(graph, tensor.Float64, gorgonia.WithShape(hiddenSize, outputSize), gorgonia.WithName("Weight2"), gorgonia.WithInit(gorgonia.Gaussian(0, 1)))
    bias1 := gorgonia.NewMatrix(graph, tensor.Float64,