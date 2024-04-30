package main

import (
	"fmt"
	"math"
)

// sigmoid wraps the main sigmoid function.
func sigmoid(x float64) float64 {
	return 1 / (1 + math.Exp(-x))
}

// computeCost calculates the cost (logistic regression loss) given features, labels, and current weights.
func computeCost(features [][]float64, labels []float64, weights []float64) float64 {
	m := 1.0
	totalCost := 0.0
	for i, featureSet := range features {
		prediction := 0.0
		for j, feature := range featureSet {
			prediction += weights[j] * feature
		}
		prediction = sigmoid(prediction)
		totalCost += -labels[i]*math.Log(prediction) - (1-labels[i])*math.Log(1-prediction)
	}
	return totalCost / m
}

// logisticRegressionUpdate updates the model's weights by performing a single iteration of gradient descent.
func logisticRegressionUpdate(features [][]float64, labels []float64, weights []float64, epsilon float64) []float64 {
	gradient := make([]float64, len(weights))
	for i, featureSet := range features {
		prediction := 0.0
		for j, feature := range featureSet {
			prediction += weights[j] * feature
		}
		error := sigmoid(prediction) - labels[i]
		for j := range weights {
			gradient[j] += error * featureSet[j]
		}
	}
	for i :=