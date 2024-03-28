
package main

import (
	"fmt"
	"github.com/sjwhitworth/golearn/base"
	"github.com/sjwhitworth/golearn/linear_models"
	"github.com/sjwhitworth/golearn/evaluation"
)

func main() {
	// Load the dataset
	rawData, err := base.ParseCSVToInstances("your_dataset.csv", true)
	if err != nil {
		panic(err)
	}

	// Initialize the SVM model
	model := linear_models.NewLinearSVC("l2", "l2", true)

	// Split the dataset into training and testing
	trainData, testData := base.InstancesTrainTestSplit(rawData, 0.75)

	// Fit the model
	err = model.Fit(trainData)
	if err != nil {
		panic(err)
	}

	// Predict
	predictions, err := model.Predict(testData)
	if err != nil {
		panic(err)
	}

	// Evaluate the model
	confusionMat, err := evaluation.GetConfusionMatrix(testData, predictions)
	if err != nil {
		panic(err)
	}

	// Print accuracy
	fmt.Println("Accuracy:", evaluation.GetAccuracy(confusionMat))
}
