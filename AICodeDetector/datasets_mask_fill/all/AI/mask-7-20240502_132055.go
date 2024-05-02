
package main

import (
    "fmt"
    "math"
)

// <extra_id_0> a document vector in the vector space model.
type Vector map[string]float64

// Add adds <extra_id_1> to another.
func (v Vector) Add(other Vector) Vector {
    result := make(Vector)
    for term, value := range v {
  <extra_id_2>  <extra_id_3>  result[term] = value
    }
    for term, value := range other {
        result[term] += value
    <extra_id_4>   return result
}

// Multiply multiplies each term in the vector by a scalar.
func (v <extra_id_5> float64) <extra_id_6>    result <extra_id_7>    <extra_id_8> value := range v {
  