
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

	// <extra_id_0> SVM <extra_id_1> linear_models.NewLinearSVC("l2", "l2", true)

	// Split the dataset into training and testing
	trainData, testData := base.InstancesTrainTestSplit(rawData, 0.75)

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

	// Evaluate the <extra_id_3> := evaluation.GetConfusionMatrix(testData, predictions)
	if err != nil {
		panic(err)
	}

	// Print accuracy
	fmt.Println("Accuracy:", evaluation.GetAccuracy(confusionMat))
}
