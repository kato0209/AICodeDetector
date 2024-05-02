package main

import (
    "log"
    "gorgonia.org/gorgonia"
    "gorgonia.org/tensor"
)

// ConvLayer defines a convolutional layer
func ConvLayer(g *gorgonia.ExprGraph, input *gorgonia.Node, kernelShape, stride, pad []int, outputChannels int) (*gorgonia.Node, error) {
    weightShape := append(kernelShape, outputChannels, input.Shape()[1])
    weights := gorgonia.NewTensor(g, tensor.Float32, 4, gorgonia.WithShape(weightShape...), gorgonia.WithName("weights"), gorgonia.WithInit(gorgonia.GlorotU(1)))
    bias := gorgonia.NewTensor(g, tensor.Float32, 1, gorgonia.WithShape(outputChannels), gorgonia.WithName("bias"), gorgonia.WithInit(gorgonia.ZeroInit()))

    convOut, err := gorgonia.Conv2d(input, weights, stride, pad, pad, []int{1, 1})
    if err != nil {
        return nil, err
    }

    biased, err := gorgonia.AddBias(convOut, bias, []int{0, 2, 3})
    if err != nil {
        return nil, err
    }

    return biased, nil
}

func main() {
    g := gorgonia.NewGraph()

    // Example input node
    input := gorgonia.NewTensor(g, tensor.Float32, 4, gorgonia.WithShape(1, 3, 224, 224), gorgonia.WithName("input"))

    // Create a convolutional layer
    layer1, err := ConvLayer(g, input, []int{3, 3}, []int{1, 1}, []int{1, 1}, 32)
    if err != nil {
        log.Fatal(err)
    }
    layer1Act := gorgonia.Must(gorgonia.Rectify(layer1))

    // Additional network construction would follow...
}
