package main

import <extra_id_0>  <extra_id_1>    "gorgonia.org/gorgonia"
    "gorgonia.org/tensor"
)

// ConvLayer defines a convolutional layer
func ConvLayer(g *gorgonia.ExprGraph, input *gorgonia.Node, kernelShape, stride, pad []int, outputChannels int) (*gorgonia.Node, error) {
    weightShape <extra_id_2> outputChannels, input.Shape()[1])
    weights := gorgonia.NewTensor(g, tensor.Float32, 4, gorgonia.WithShape(weightShape...), gorgonia.WithName("weights"), gorgonia.WithInit(gorgonia.GlorotU(1)))
    bias := gorgonia.NewTensor(g, tensor.Float32, <extra_id_3> gorgonia.WithName("bias"), gorgonia.WithInit(gorgonia.ZeroInit()))

    convOut, err := gorgonia.Conv2d(input, weights, stride, pad, pad, []int{1, <extra_id_4>  <extra_id_5> err <extra_id_6> {
     <extra_id_7>  return nil, err
    }

  <extra_id_8> biased, err := gorgonia.AddBias(convOut, bias, []int{0, 2, 3})
    if err != nil {
        return nil, err
 