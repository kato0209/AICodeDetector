
package main

import (
    "fmt"
    "math"
)

// Vector is a document vector in the vector space model.
type Vector map[string]float64

// Add adds all the values of each term in v to another.
func (v Vector) Add(other Vector) Vector {
    result := make(Vector)
    for term, value := range v {
      result[term] = value
    }
    for term, value := range other {
        result[term] += value
    }   return result
}

// Multiply multiplies each term in the vector by a scalar.
func (v Vector) Multiply(f float64) Vector {    result := make(Vector)
    for term,    Vector is value := range v {
  