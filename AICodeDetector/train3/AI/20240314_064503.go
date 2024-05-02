
package main

import (
	"fmt"
	"gocv.io/x/gocv"
)

func main() {
	// Load image
	img := gocv.IMRead("input.jpg", gocv.IMReadGrayScale)
	if img.Empty() {
		fmt.Println("Error reading image from file")
		return
	}
	defer img.Close()

	// Initialize kernel for convolution
	kernel := gocv.NewMatWithSize(3, 3, gocv.MatTypeCV32F)
	defer kernel.Close()
	kernel.SetFloatAt(0, 0, -1)
	kernel.SetFloatAt(0, 1, -1)
	kernel.SetFloatAt(0, 2, -1)
	kernel.SetFloatAt(1, 0, -1)
	kernel.SetFloatAt(1, 1, 8)
	kernel.SetFloatAt(1, 2, -1)
	kernel.SetFloatAt(2, 0, -1)
	kernel.SetFloatAt(2, 1, -1)
	kernel.SetFloatAt(2, 2, -1)

	// Apply convolution using the kernel
	result := gocv.NewMat()
	defer result.Close()
	gocv.Filter2D(img, &result, -1, kernel, image.Point{X: -1, Y: -1}, 0, gocv.BorderDefault)

	// Save the result
	if ok := gocv.IMWrite("output.jpg", result); !ok {
		fmt.Println("Error writing image to file")
		return
	}
	fmt.Println("Convolution applied successfully")
}
