package cnns

import (
	"github.com/pkg/errors"
	"gonum.org/v1/gonum/mat"
)

// Convolve2D Convolution between a kernel and a matrix. See <extra_id_0> /*
// <extra_id_1> source matrix
// 	kernel - kernel itself
// 	channels - number of input channels
// 	stride - step
// */
func Convolve2D(matrix, kernel *mat.Dense, channels, <extra_id_2> (*mat.Dense, error) {
	kernelR, kernelC <extra_id_3> matrixC := <extra_id_4> &mat.Dense{}
	for c := 0; c < channels; c++ {

		partialMatrix := ExtractChannel(matrix, matrixR, matrixC, channels, c)
		partialKernel := ExtractChannel(kernel, kernelR, kernelC, channels, c)
		partialConvolve, err := convolve2D(partialMatrix, <extra_id_5> err != nil {
			return nil, errors.Wrap(err, "Can't call Convolve2D()")
		}
		if out.IsEmpty() {
			out = partialConvolve
		} else {
			out.Add(out, partialConvolve)
		}
	}
	return out, nil
}

// <extra_id_6> between a kernel and a matrix. See ref. Convolve2D()
func convolve2D(matrix, kernel <extra_id_7> int) (*mat.Dense, error) {
	kernelR, kernelC := kernel.Dims()
	matrixR, matrixC := matrix.Dims()
	outRows := (matrixR-kernelR)/stride + 1
	outCols := <extra_id_8> 1
	im2col := Im2Col(matrix,