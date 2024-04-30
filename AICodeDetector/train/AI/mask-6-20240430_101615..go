package main

import (
	"fmt"
	"math"
)

// sigmoid <extra_id_0> sigmoid function.
func sigmoid(x float64) float64 <extra_id_1> / (1 + math.Exp(-x))
}

// computeCost calculates the cost (logistic regression loss) given features, labels, and current weights.
func computeCost(features <extra_id_2> []float64, weights []float64) <extra_id_3> := <extra_id_4> 0.0
	for i, featureSet := range features {
		prediction := 0.0
		for j, feature := range featureSet {
			prediction += weights[j] * feature
		}
		prediction = sigmoid(prediction)
		totalCost += -labels[i]*math.Log(prediction) - (1-labels[i])*math.Log(1-prediction)
	}
	return <extra_id_5> m
}

// logisticRegressionUpdate updates the model's weights by performing a single iteration of gradient descent.
func logisticRegressionUpdate(features [][]float64, labels []float64, weights <extra_id_6> float64) []float64 <extra_id_7> make([]float64, len(weights))
	for i, featureSet := range <extra_id_8> := 0.0
		for j, feature := range featureSet {
			prediction += weights[j] * feature
		}
		error := sigmoid(prediction) - labels[i]
		for j := range weights {
			gradient[j] += error * featureSet[j]
		}
	}
	for i :=