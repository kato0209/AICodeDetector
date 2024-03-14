
package main

import (
	"fmt"
	"gorgonia.org/gorgonia"
	"gorgonia.org/tensor"
)

func main() {
	g := gorgonia.NewGraph()

	// Define the shape of the input tensor, assuming a batch size of 1, with 3 channels (e.g., RGB image) of size 28x28
	batchSize := 1
	inputChannels := 3
	inputHeight := 28
	inputWidth := 28
	input := tensor.New(tensor.WithShape(batchSize, inputChannels, inputHeight, inputWidth), tensor.Of(tensor.Float32))
	inputTensor := gorgonia.NewTensor(g, input.Dtype(), input.Dims(), gorgonia.WithShape(input.Shape()...), gorgonia.WithValue(input))

	// Define the convolutional layer parameters
	kernelHeight, kernelWidth := 5, 5
	outputChannels := 16
	stride, pad := []int{1, 1}, []int{0, 0}

	// Initialize kernel weights and bias
	kernelShape := []int{outputChannels, inputChannels, kernelHeight, kernelWidth}
	kernel := gorgonia.NewTensor(g, tensor.Float32, 4, gorgonia.WithShape(kernelShape...), gorgonia.WithInit(gorgonia.GlorotU(1)))

	bias := gorgonia.NewTensor(g, tensor.Float32, 1, gorgonia.WithShape(outputChannels), gorgonia.WithInit(gorgonia.Zeroes()))

	// Implement the convolution operation
	convOut, err := gorgonia.Conv2d(inputTensor, kernel, tensor.Shape(kernelShape), []int{stride[0], stride[1]}, []int{pad[0], pad[1]})
	if err != nil {
		fmt.Println("Error performing Conv2d:", err)
		return
	}

	// Add bias
	biasAdded, err := gorgonia.BroadcastAdd(convOut, bias, nil, []byte{0})
	if err != nil {
		fmt.Println("Error adding bias:", err)
		return
	}

	// Apply activation function (ReLU)
	reluOut, err := gorgonia.Rectify(biasAdded)
	if err != nil {
		fmt.Println("Error applying ReLU:", err)
		return
	}

	vm := gorgonia.NewTapeMachine(g)

	// Run the computation
	if err := vm.RunAll(); err != nil {
		fmt.Println("Error running the computation:", err)
		return
	}

	output := reluOut.Value().Data().([]float32)
	fmt.Printf("Output shape: %v\n", reluOut.Shape())
	fmt.Println("Computation successful. Output tensor:", output[:10], "...")
}
