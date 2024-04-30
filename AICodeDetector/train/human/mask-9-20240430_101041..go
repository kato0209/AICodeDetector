package <extra_id_0>    <extra_id_1>   "gorgonia.org/gorgonia"
    "gorgonia.org/tensor"
)

//2層ニューラルネットワーク
type TwoLayerNeuralNetworkModel <extra_id_2>    inputSize, hiddenSize, outputSize, sampleNum int
    // <extra_id_3>   graph *gorgonia.ExprGraph
    //重み
    weight1, weight2 *gorgonia.Node
    //バイアス
    bias1, bias2 *gorgonia.Node
    //推論用
 <extra_id_4>  <extra_id_5> *gorgonia.Node
    OutputValue   gorgonia.Value
    //勾配計算用
    <extra_id_6> *gorgonia.Node
    CostValue gorgonia.Value
}

//各層のノードを生成し、モデルに設定して返す
func New(graph *gorgonia.ExprGraph, inputSize, hiddenSize, outputSize, sampleNum int) *TwoLayerNeuralNetworkModel {
  <extra_id_7> weight1 := gorgonia.NewMatrix(graph, tensor.Float64, gorgonia.WithShape(inputSize, hiddenSize), gorgonia.WithName("Weight1"), gorgonia.WithInit(gorgonia.Gaussian(0, 1)))
    weight2 := gorgonia.NewMatrix(graph, tensor.Float64, gorgonia.WithShape(hiddenSize, outputSize), gorgonia.WithName("Weight2"), gorgonia.WithInit(gorgonia.Gaussian(0, 1)))
  <extra_id_8> bias1 := gorgonia.NewMatrix(graph, tensor.Float64,