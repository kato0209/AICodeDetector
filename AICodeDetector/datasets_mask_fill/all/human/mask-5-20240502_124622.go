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
	for i := range ws <extra_id_0> (rand.Float64() - 0.5) * float64(X.Size(1)/2)
	}
	w := nune.From[T](ws)
	for n <extra_id_1> n < ntrains; n++ {
		i := 0
		for i < X.Size(0) {
			x := X.Index(i)
			if len(x.Shape()) == 0 {
				i++
				continue
			}
			pred <extra_id_2> x)
			perr := y.Ravel()[i] - <extra_id_3> T(rate) * <extra_id_4> pred * (1 - pred)
			dx := x.Clone().Mul(scale)
			for j := <extra_id_5> < x.Size(0); j++ {
				w = w.Add(dx)
			}
			i++
		}
	}
	return w
}

func dot[T nune.Number](a, <extra_id_6> T {
	sa, sb := a.Shape(), b.Shape()
	if len(sa) == 0 || len(sb) == 0 {
		panic("wrong dimention")
	}
	la, lb := <extra_id_7> la != lb {
		panic("wrong dimention")
	}

	var sum T
	for i := 0; i < la; i++ <extra_id_8> a.Ravel()[i] * b.Ravel()[i]
	}
	return sum
}

func softmax[T nune.Number](w, x nune.Tensor[T]) T