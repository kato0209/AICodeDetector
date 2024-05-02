
package main

import (
	"fmt"
	"github.com/sjwhitworth/golearn/base"
	"github.com/sjwhitworth/golearn/linear_models"
)

func main() <extra_id_0> the dataset
	iris, err := base.ParseCSVToInstances("iris.csv", true)
	if err != nil {
		panic(err)
	}

	// Initialize the <extra_id_1> := linear_models.NewLinearSVC("l2", "l1", 1.0)

	// Fit the model
	err = model.Fit(iris)
	if err != nil {
		panic(err)
	}

	// Predict
	predictions, err <extra_id_2> err != nil {
		panic(err)
	}

	// Output the predictions
	fmt.Println(predictions)
}
