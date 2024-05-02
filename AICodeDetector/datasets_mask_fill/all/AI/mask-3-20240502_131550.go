
package main

import (
	"gorgonia.org/gorgonia"
	"gorgonia.org/tensor"
)

func <extra_id_0> Create <extra_id_1> graph
	g := gorgonia.NewGraph()

	// Define the <extra_id_2> shape (batchSize, channels, height, width)
	input := tensor.New(tensor.Of(tensor.Float32), tensor.WithShape(1, 1, 28, <extra_id_3> gorgonia.NodeFromAny(g, input, gorgonia.WithName("input"))

	// Define the kernel tensor shape (outputChannels, inputChannels, height, width)
	kernel := tensor.New(tensor.Of(tensor.Float32), tensor.WithShape(1, 1, 5, 5))
	kernelNode := gorgonia.NodeFromAny(g, kernel, gorgonia.WithName("kernel"))

	// Perform 2D convolution
	convOut, err := gorgonia.Conv2d(inputNode, <extra_id_4> 5}, []int{1, 1}, []int{0, 0}, []int{1, 1})
	if err != nil {
		panic(err)
	}

	// Compile the <extra_id_5> gorgonia.NewTapeMachine(g)

	// Run the graph
	if err := machine.RunAll(); err != nil {
		panic(err)
	}
}
