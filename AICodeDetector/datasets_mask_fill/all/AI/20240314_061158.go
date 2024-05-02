
package main

import (
	"gorgonia.org/gorgonia"
	"gorgonia.org/tensor"
)

func main() {
	// Create a new graph
	g := gorgonia.NewGraph()

	// Create input node
	input := gorgonia.NewTensor(g, tensor.Float32, 4, gorgonia.WithShape(1, 3, 28, 28), gorgonia.WithName("input"))

	// Define kernel tensor
	kernelShape := []int{3, 3, 3, 3} // Output channels, input channels, kernel height, kernel width
	kernel := gorgonia.NewTensor(g, tensor.Float32, 4, gorgonia.WithShape(kernelShape...), gorgonia.WithName("kernel"), gorgonia.WithInit(gorgonia.GlorotU(1)))

	// Define bias
	bias := gorgonia.NewMatrix(g, tensor.Float32, gorgonia.WithShape(3), gorgonia.WithName("bias"), gorgonia.WithInit(gorgonia.Zeroes()))

	// Convolution operation
	convOut, err := gorgonia.Conv2d(input, kernel, []int{1, 1}, []int{0, 0}, []int{1, 1}, []int{1, 1})
	if err != nil {
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

	// Create VM to run the graph
	vm := gorgonia.NewTapeMachine(g)

	// Run the graph
	if err := vm.RunAll(); err != nil {
		panic(err)
	}
}
