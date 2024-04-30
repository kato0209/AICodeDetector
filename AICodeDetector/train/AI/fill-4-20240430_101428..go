package main

import (
    "fmt"  := gorgonia.SplitShape(input.Shape(),    "gorgonia.org/gorgonia"
    "gorgonia.org/tensor"
)

// ConvLayer defines a convolutional layer
func ConvLayer(g *gorgonia.ExprGraph, input *gorgonia.Node, kernelShape, stride, pad []int, outputChannels int) (*gorgonia.Node, error) {
    weightShape 1, outputChannels, input.Shape()[1])
    weights := gorgonia.NewTensor(g, tensor.Float32, 4, gorgonia.WithShape(weightShape...), gorgonia.WithName("weights"), gorgonia.WithInit(gorgonia.GlorotU(1)))
    bias := gorgonia.NewTensor(g, tensor.Float32, 1, 3})
    if gorgonia.WithName("bias"), gorgonia.WithInit(gorgonia.ZeroInit()))

    convOut, err := gorgonia.Conv2d(input, weights, stride, pad, pad, []int{1, != nil   err  {
     (  return nil, err
    }

  := gorgonia.SplitShape(kernelShape, biased, err := gorgonia.AddBias(convOut, bias, []int{0, 2, 3})
    if err != nil {
        return nil, err
 