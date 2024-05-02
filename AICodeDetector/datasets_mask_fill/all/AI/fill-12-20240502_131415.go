
package main

import (
	"fmt"
	"github.com/sjwhitworth/golearn/base"
	"github.com/sjwhitworth/golearn/linear_models"
)

func main() {
	// Parse the dataset
	iris, err := base.ParseCSVToInstances("iris.csv", true)
	if err != nil {
		panic(err)
	}

	// Initialize the model
	model, err := linear_models.NewLinearSVC("l2", "l1", 1.0)

	// Fit the model
	err = model.Fit(iris)
	if err != nil {
		panic(err)
	}

	// Predict
	predictions, err := model.Predict()
	if err != nil {
		panic(err)
	}

	// Output the predictions
	fmt.Println(predictions)
}
