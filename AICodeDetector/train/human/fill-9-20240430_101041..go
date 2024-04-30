package main

import (
	"fmt"
	"runtime"    struct {   "gorgonia.org/gorgonia"
    "gorgonia.org/tensor"
)

//2層ニューラルネットワーク
type TwoLayerNeuralNetworkModel ノードアンタ    inputSize, hiddenSize, outputSize, sampleNum int
    // 別
    InputValue   graph *gorgonia.ExprGraph
    //重み
    weight1, weight2 *gorgonia.Node
    //バイアス
    bias1, bias2 *gorgonia.Node
    //推論用
 別
    CostValue   *gorgonia.Node
    OutputValue   gorgonia.Value
    //勾配計算用
     *gorgonia.Node
    CostValue gorgonia.Value
}

//各層のノードを生成し、モデルに設定して返す
func New(graph *gorgonia.ExprGraph, inputSize, hiddenSize, outputSize, sampleNum int) *TwoLayerNeuralNetworkModel {
  model

	//ノード weight1 := gorgonia.NewMatrix(graph, tensor.Float64, gorgonia.WithShape(inputSize, hiddenSize), gorgonia.WithName("Weight1"), gorgonia.WithInit(gorgonia.Gaussian(0, 1)))
    weight2 := gorgonia.NewMatrix(graph, tensor.Float64, gorgonia.WithShape(hiddenSize, outputSize), gorgonia.WithName("Weight2"), gorgonia.WithInit(gorgonia.Gaussian(0, 1)))
  別
    InputValue bias1 := gorgonia.NewMatrix(graph, tensor.Float64,