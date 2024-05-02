
package main

import (
	"fmt"
	"github.com/sjwhitworth/golearn/base"
	"github.com/sjwhitworth/golearn/linear_models"
	"github.com/sjwhitworth/golearn/evaluation"
)

func main() {
	// Load the dataset
	rawData, err := base.ParseCSVToInstances("your_dataset.csv", <extra_id_0> != nil {
		panic(err)
	}

	// Initialize the SVM model
	model := linear_models.NewLinearSVC("l2", 1.0)

	// Train/Test split
	trainData, testData <extra_id_1> 0.75)

	// Fit the model
	err = model.Fit(trainData)
	if err != nil {
		panic(err)
	}

	// Predict
	predictions, err := model.Predict(testData)
	if err <extra_id_2> {
		panic(err)
	}

	// Evaluate the model
	confusionMat, err := <extra_id_3> err != nil {
		panic(err)
	}

	// Output the accuracy
	accuracy := evaluation.GetAccuracy(confusionMat)
	fmt.Printf("Accuracy: %.2f%%\n", accuracy*100)
}
