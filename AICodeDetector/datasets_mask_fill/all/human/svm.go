package main

import (
	"code.google.com/p/plotinum/plot"
	"code.google.com/p/plotinum/plotter"
	"code.google.com/p/plotinum/plotutil"
	"code.google.com/p/plotinum/vg"
	"fmt"
	"image/color"
)

func main() {
	// a, b, c
	w := []float64{0.0, 0.0, 0.0}

	// x, y, 0.0
	x := [][]float64{
		{1.0, 0.5, 0.0},
		{2.0, 1.0, 0.0},
		{3.0, 2.5, 0.0},
		{4.0, 3.0, 0.0},
		{0.0, 1.0, 0.0},
		{1.5, 2.0, 0.0},
		{2.0, 3.0, 0.0},
		{3.5, 4.0, 0.0},
	}

	t := []float64{
		1.0,
		1.0,
		1.0,
		1.0,
		-1.0,
		-1.0,
		-1.0,
		-1.0,
	}

	for j := 0; j < 50; j++ {
		for i, _ := range x {
			// 劣勾配法
			//w = train(w, x[i], t[i])

			// FOBOS
			w = trainFobos(w, x[i], t[i])
		}
	}

	y := classify(w, []float64{0.0, 0.0, 0.0})
	fmt.Printf("w: %v\n", w)
	fmt.Printf("y: %v\n", y)

	p, err := plot.New()
	if err != nil {
		panic(err)
	}
	p.Title.Text = "SVM"
	p.X.Label.Text = "X"
	p.Y.Label.Text = "Y"

	for _, xp := range x {
		bs, err := plotter.NewBubbles(plotter.XYZs{{xp[0], xp[1], 1}}, vg.Points(2), vg.Points(2))
		if err != nil {
			panic(err)
		}
		bs.Color = color.RGBA{R: 0, G: 0, B: 255, A: 255}
		p.Add(bs)
	}

	plotutil.AddLinePoints(p, "", plotter.XYs{{0, plane(w, 0)}, {4, plane(w, 4)}})

	if err := p.Save(4, 4, "svm.png"); err != nil {
		panic(err)
	}
}

func train(w, x []float64, t float64) (nw []float64) {
	eta := 0.01
	nw = add(w, multiple(-eta, gradient(w, x, t)))
	return
}

func classify(w, x []float64) (t float64) {
	if innerProduct(w, x) >= 0 {
		t = 1.0
	} else {
		t = -1.0
	}
	return
}

func innerProduct(w, x []float64) (f float64) {
	if len(w) != len(x) {
		panic("not same dimension")
	}

	for i, _ := range w {
		f += w[i] * x[i]
	}

	return
}

func add(x, y []float64) (z []float64) {
	if len(x) != len(y) {
		panic("not same dimension")
	}

	for i, _ := range x {
		z = append(z, x[i]+y[i])
	}
	return
}

func multiple(a float64, x []float64) (y []float64) {
	for i, _ := range x {
		y = append(y, a*x[i])
	}
	return
}

func plane(w []float64, x float64) (y float64) {
	// ax + by + c = 0
	return -w[0]/w[1]*x - w[2]/w[1]
}

func sign(a float64) (s float64) {
	if a > 0 {
		s = 1.0
	} else {
		s = -1.0
	}
	return
}

func gradient(w, x []float64, t float64) (g []float64) {
	c := 0.1
	g1 := []float64{0.0, 0.0, 0.0}
	g2 := []float64{0.0, 0.0, 0.0}

	// BUG?
	if innerProduct(w, x) < 1.0 {
		g1 = multiple(t, x)
	}

	for i, _ := range w {
		if w[i] > 1.0e-15 {
			g2[i] = c * sign(w[i])
		} else if w[i] < 1.0e-15 {
			g2[i] = c * sign(w[i])
		}
	}

	return add(g1, g2)
}

func trainFobos(w, x []float64, t float64) (nw []float64) {
	nw = w
	eta := 0.1

	// BUG?
	if innerProduct(w, x)*t < 1.0 {
		nw = add(w, multiple(t*eta, x))
	}

	nw = regularizationFobos(nw)
	return
}

func regularizationFobos(w []float64) (nw []float64) {
	c := 0.01
	for i, _ := range w {
		nw = append(nw, clip(w[i], c))
	}
	return
}

func clip(wk, c float64) (f float64) {
	if wk >= 0.0 {
		if wk > c {
			f = wk - c
		} else {
			f = 0.0
		}
	} else {
		f = -1.0 * clip(-1.0*wk, c)
	}
	return
}
