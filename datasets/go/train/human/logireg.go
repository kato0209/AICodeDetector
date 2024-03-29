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
			pred := softmax(w, x)
			perr := y.Ravel()[i] - pred
			scale := T(rate) * perr * pred * (1 - pred)
			dx := x.Clone().Mul(scale)
			for j := 0; j < x.Size(0); j++ {
				w = w.Add(dx)
			}
			i++
		}
	}
	return w
}

func dot[T nune.Number](a, b nune.Tensor[T]) T {
	sa, sb := a.Shape(), b.Shape()
	if len(sa) == 0 || len(sb) == 0 {
		panic("wrong dimention")
	}
	la, lb := sa[0], sb[0]
	if la != lb {
		panic("wrong dimention")
	}

	var sum T
	for i := 0; i < la; i++ {
		sum += a.Ravel()[i] * b.Ravel()[i]
	}
	return sum
}

func softmax[T nune.Number](w, x nune.Tensor[T]) T {
	v := dot(w, x)
	return T(1.0 / (1.0 + math.Exp(float64(-v))))
}

func predict[T nune.Number](w, x nune.Tensor[T]) T {
	return softmax(w, x)
}

func loadData() ([][]float64, []string, error) {
	f, err := os.Open("iris.csv")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	var resultV [][]float64
	var resultS []string

	scanner := bufio.NewScanner(f)
	// skip header
	scanner.Scan()
	for scanner.Scan() {
		var f1, f2, f3, f4 float64
		var s string
		n, err := fmt.Sscanf(scanner.Text(), "%f,%f,%f,%f,%s", &f1, &f2, &f3, &f4, &s)
		if n != 5 || err != nil {
			continue
		}
		resultV = append(resultV, []float64{f1, f2, f3, f4})
		resultS = append(resultS, s)
	}

	if err = scanner.Err(); err != nil {
		return nil, nil, err
	}
	return resultV, resultS, nil
}

func shuffle[X any, Y any](xx []X, yy []Y) {
	n := len(xx)
	for i := n - 1; i >= 0; i-- {
		j := rand.Intn(i + 1)
		xx[i], xx[j] = xx[j], xx[i]
		yy[i], yy[j] = yy[j], yy[i]
	}
}

func vocab(nn []string) map[string]int {
	m := make(map[string]int)
	for _, n := range nn {
		if _, ok := m[n]; !ok {
			m[n] = len(m)
		}
	}
	return m
}

func onehot[T nune.Number](aa []string, nn map[string]int) nune.Tensor[T] {
	v := nune.Zeros[T](len(aa))
	for i := 0; i < len(aa); i++ {
		f, ok := nn[aa[i]]
		if ok {
			v.Ravel()[i] = T(f)
		}
	}
	return v.Mul(1 / float64(len(nn)))
}

func main() {
	X, Y, err := loadData()
	if err != nil {
		log.Fatal(err)
	}

	ns := vocab(Y)
	m := make([]string, len(ns))
	for k, v := range ns {
		m[v] = k
	}

	shuffle(X, Y)
	n := 100
	xtrain, ytrain, xtest, ytest := X[:n], Y[:n], X[n:], Y[n:]

	Xn := nune.From[float64](xtrain)
	Yn := onehot[float64](ytrain, ns)

	Wn := logisticRegression(Xn, Yn, 0.01, 5000)

	c := 0
	for i, test := range xtest {
		pred := softmax(Wn, nune.From[float64](test))
		p := int(pred*3 + 0.5)
		fmt.Println(m[p], ytest[i])
		if m[p] == ytest[i] {
			c++
		}
	}
	fmt.Printf("Accuracy %f\n", float64(c)/float64(len(xtest)))
}
