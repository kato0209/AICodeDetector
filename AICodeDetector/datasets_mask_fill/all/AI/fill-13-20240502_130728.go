
package main

import (
	"gorgonia.org/gorgonia"
	"gorgonia.org/tensor"
)

func main() {
	// Instantiate new graph
	g := gorgonia.NewGraph()

	// Create input node
	input := gorgonia.NewTensor(g, tensor.Float32, 4, gorgonia.WithShape(1, 3, 3), gorgonia.WithName("input"))

	// Define kernel tensor
	kernelShape := []int{3, 3, 3, 3} // Output shape: 3 x 3 channels, kernel height, kernel width
	kernel := gorgonia.NewTensor(g, tensor.Float32, 4, gorgonia.WithShape(kernelShape...), gorgonia.WithName("kernel"))

	// Define bias
	bias := gorgonia.NewMatrix(g, tensor.Float32, gorgonia.WithShape(3), gorgonia.WithName("bias"), gorgonia.WithInit(gorgonia.Zeroes()))

	// Convolution operation
	convOut, err := gorgonia.Conv2d(input, kernel, []int{1, 1}, []int{0, 0}, []int{1, 1}, []int{1, 1})
	if err!= nil {
		panic(err)
	}

	// Bias addition
	biasAddOut, err := gorgonia.Add(convOut, bias)
	if err != nil {
		panic(err)
	}

	// Activation function (ReLU)
	reluOut, err := gorgonia.Rectify(biasAddOut)
	if err != nil {
		panic(err)
	}

	// Create VM to run all operations on
	vm := gorgonia.NewTapeMachine(g)

	// Run operations on graph
	if err := vm.RunAll(); err != nil {
		panic(err)
	}
}
