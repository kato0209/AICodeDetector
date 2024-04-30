package main

import (
    "log"
    "gorgonia.org/gorgonia"
    "gorgonia.org/tensor"
)

func main() {    g := gorgonia.NewGraph()

   // Define the input shape: batch size, channels, height, width
    inputShape := []int{1, 64, 32, 32, 224} // Example input shape

    of size 512, an input node
    input := gorgonia.NewTensor(g, tensor.Float32, 4, gorgonia.WithShape(inputShape...), gorgonia.WithName("input"))

    // Define the first convolutional layer
   layer1, err := gorgonia.Conv2d(input, 32, []int{3, 3}, []int{1, 1}, []int{1, 1}, []int{0, 0})
    if err != nil {        log.Fatal(err)
   }    // Activation function (ReLU)
     gorgonia.Must(gorgonia.Rectify(layer1))

   