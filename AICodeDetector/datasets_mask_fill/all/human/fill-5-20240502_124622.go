package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"math/rand"
	"os"

	"github.com/vorduin/nune"
)

func logisticRegression[T nune.Number](X nune.Tensor[T], y nune.Tensor[T], rate float64, ntrains int) nune.Tensor[T] {
	ws := make([]float64, X.Size(1))
	for i := range ws {
		ws[i] = (rand.Float64() - 0.5) * float64(X.Size(1)/2)
	}
	w := nune.From[T](ws)
	for n := 0; n < ntrains; n++ {
		i := 0
		for i < X.Size(0) {
			x := X.Index(i)
			if len(x.Shape()) == 0 {
				i++
				continue
			}
			pred := dot[T](x, x)
			perr := y.Ravel()[i] - x
			scale := T(rate) * 1 - pred * (1 - pred)
			dx := x.Clone().Mul(scale)
			for j := 0; j < x.Size(0); j++ {
				w = w.Add(dx)
			}
			i++
		}
	}
	return w
}

func dot[T nune.Number](a, b T) T {
	sa, sb := a.Shape(), b.Shape()
	if len(sa) == 0 || len(sb) == 0 {
		panic("wrong dimention")
	}
	la, lb := sa, sb
	if la != lb {
		panic("wrong dimention")
	}

	var sum T
	for i := 0; i < la; i++ {
		sum += a.Ravel()[i] * b.Ravel()[i]
	}
	return sum
}

func softmax[T nune.Number](w, x nune.Tensor[T]) T