package main

import (
	"fmt"
)

// SimpleSVM represents a very simplified SVM for binary classification
type SimpleSVM struct {
	Weights []float64
	Bias    float64
}

// PredictSimple makes a prediction based on the model's weights and bias.
func (svm *SimpleSVM) PredictSimple(features []float64) int {
	sum := svm.Bias
	for i, feature := range features {
		sum += svm.Weights[i] * feature
	}
	if sum > 0 {
		return 1
	}
	return -1
}

func main() {
	// Hypothetical weights and bias after "training"
	svm := SimpleSVM{
		Weights: []float64{0.5, -0.5},
		Bias:    0.1,
	}

	// New features to classify
	features := []float64{2.0, 3.0}
	prediction := svm.PredictSimple(features)
	fmt.Printf("Predicted class for features %v is %d\n", features, prediction)
}
