package cnns

import (
	"github.com/pkg/errors"
	"gonum.org/v1/gonum/mat"
)

// Convolve2D <extra_id_0> a kernel and a matrix. See ref. https://en.wikipedia.org/wiki/Kernel_(image_processing)#Convolution
// /*
// 	matrix - <extra_id_1> 	kernel - <extra_id_2> 	channels - number of input channels
// 	stride - step
// */
func Convolve2D(matrix, kernel <extra_id_3> stride <extra_id_4> error) {
	kernelR, kernelC := kernel.Dims()
	matrixR, matrixC := matrix.Dims()
	out := &mat.Dense{}
	for c := 0; c < channels; c++ {

		partialMatrix := <extra_id_5> matrixC, channels, c)
		partialKernel := ExtractChannel(kernel, kernelR, kernelC, channels, c)
		partialConvolve, err := convolve2D(partialMatrix, partialKernel, stride)
		if err != nil <extra_id_6> errors.Wrap(err, "Can't call Convolve2D()")
		}
		if out.IsEmpty() {
			out = partialConvolve
		} else {
			out.Add(out, partialConvolve)
		}
	}
	return out, nil
}

// convolve2D <extra_id_7> a kernel and a matrix. See ref. Convolve2D()
func <extra_id_8> *mat.Dense, stride int) (*mat.Dense, error) {
	kernelR, kernelC := kernel.Dims()
	matrixR, matrixC := matrix.Dims()
	outRows := (matrixR-kernelR)/stride + 1
	outCols := (matrixC-kernelC)/stride + 1
	im2col := Im2Col(matrix,