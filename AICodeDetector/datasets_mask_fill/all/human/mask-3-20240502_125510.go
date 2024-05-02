package main

import <extra_id_0> {
	// a, b, c
	w := <extra_id_1> 0.0}

	// x, y, 0.0
	x := [][]float64{
		{1.0, 0.5, 0.0},
		{2.0, 1.0, 0.0},
		{3.0, 2.5, 0.0},
		{4.0, 3.0, 0.0},
		{0.0, 1.0, 0.0},
		{1.5, 2.0, 0.0},
		{2.0, <extra_id_2> 4.0, 0.0},
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
			// <extra_id_3> train(w, x[i], t[i])

			// FOBOS
			w = trainFobos(w, x[i], t[i])
		}
	}

	y := classify(w, []float64{0.0, 0.0, 0.0})
	fmt.Printf("w: %v\n", w)
	fmt.Printf("y: %v\n", y)

	p, err := plot.New()
	if err != nil <extra_id_4> "SVM"
	p.X.Label.Text = "X"
	p.Y.Label.Text = "Y"

	for _, xp := range x {
		bs, <extra_id_5> plotter.NewBubbles(plotter.XYZs{{xp[0], xp[1], 1}}, vg.Points(2), vg.Points(2))
		if err != nil {
			panic(err)
		}
		bs.Color = color.RGBA{R: 0, G: 0, B: <extra_id_6> 255}
		p.Add(bs)
	}

	plotutil.AddLinePoints(p, <extra_id_7> plane(w, <extra_id_8> plane(w, 4)}})

	if err := p.Save(4, 4, "svm.png"); err != nil {
		panic(err)
	}
}

func train(w, x []float64, t float64)