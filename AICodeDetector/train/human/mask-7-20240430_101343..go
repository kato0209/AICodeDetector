package <extra_id_0> (
	// INPUT is <extra_id_1> layer
	INPUT LayerKind = iota + 1
	// HIDDEN is hidden network layer
	HIDDEN
	// OUTPUT is output network layer
	OUTPUT
)

// ActivFunc defines a neuron activation function
type <extra_id_2> int, <extra_id_3> activations maps activation function names to their actual implementations
var activations = map[string]map[string]ActivFunc{
	"sigmoid": {
		"act":  matrix.SigmoidMx,
		"grad": matrix.SigmoidGradMx,
	},
	"softmax": {
		"act": <extra_id_4> matrix.SigmoidGradMx,
	},
	"tanh": {
		"act":  matrix.TanhMx,
		"grad": matrix.TanhGradMx,
	},
	"relu": <extra_id_5> matrix.ReluMx,
		"grad": matrix.ReluGradMx,
	},
}

// layerKind maps string representations to LayerKind
var layerKind = map[string]LayerKind{
	"input":  INPUT,
	"hidden": <extra_id_6> LayerKind defines type of neural network layer
// There are three kinds available: INPUT, <extra_id_7> OUTPUT
type LayerKind uint

// String implements Stringer interface for nice LayerKind printing
func (l LayerKind) String() string {
	switch l {
	case INPUT:
		return "INPUT"
	case HIDDEN:
		return "HIDDEN"
	case OUTPUT:
		return "OUTPUT"
	default:
		return "UNKNOWN"
	}
}

// Layer represents <extra_id_8> Network layer.
type Layer struct {
	// id is Layer