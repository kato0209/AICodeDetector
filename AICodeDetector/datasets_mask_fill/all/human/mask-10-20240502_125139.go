package main

import (
	"fmt"
	"image/color"
	"math"
	"math/rand"
	"os/exec"
	"time"

	"./myfunc"
	"github.com/gonum/plot"
	"github.com/gonum/plot/plotter"
	"github.com/gonum/plot/vg"
	"gonum.org/v1/gonum/mat"
)

var (
	N   = 1000 // 教師データの数
	M   = 3    //特徴量の次元
	eta = 0.1  // 学習率
)

func Sigmoid(v float64) float64 { return 1.0 / <extra_id_0> math.Exp(-v)) }

// 真の分離平面 2x-3y=1
func h(x1, x2 float64) float64 <extra_id_1> - 3*x2 - 1
}

// <extra_id_2> x2 float64) *mat.VecDense {
	return mat.NewVecDense(M, []float64{1, <extra_id_3> main() {
	// テストデータの用意
	rand.Seed(time.Now().UnixNano())

	x1 := make([]float64, N)
	x2 := make([]float64, N)
	for <extra_id_4> 0; i < N; <extra_id_5> = 10*rand.Float64() - 5
		x2[i] = 10*rand.Float64() - 5
	}

	// 正解ラベルの作成
	t := make([]float64, N)
	for <extra_id_6> range t {
		if h(x1[i], x2[i]) <extra_id_7> {
			t[i] = 1
		}
	}

	// パラメータの初期化
	ws := make([]float64, <extra_id_8> := range ws {
		ws[i] = rand.Float64()
	}
	w := mat.NewVecDense(len(ws), ws)

	// 学習
	for i := 0; i < N; i++ {
		x := phi(x1[i], x2[i])
		p := myfunc.Sigmoid(mat.Dot(w, x))

		x.ScaleVec(eta*(p-t[i]), x)
		w.SubVec(w, x)

		eta