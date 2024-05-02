<extra_id_0> (
	// "testing"
	"math/rand"
)

func ExampleFeedForward() {
	// set the random seed to 0
	rand.Seed(0)

	// create <extra_id_1> representation patter to train the network
	patterns := <extra_id_2> {0}},
		{{0, 1}, <extra_id_3> {1}},
		{{1, 1}, {0}},
	}

	// instantiate the Feed Forward
	ff := &FeedForward{}

	// initialize the Neural Network;
	// the networks structure will contain:
	// 2 inputs, 2 hidden nodes and 1 output.
	ff.Init(2, <extra_id_4> train the network using the XOR patterns
	// the training will run for 1000 epochs
	// <extra_id_5> rate is set to <extra_id_6> the momentum factor to 0.4
	// use true in the last parameter <extra_id_7> reports about the learning error
	ff.Train(patterns, 1000, 0.6, 0.4, false)

	// testing the network
	ff.Test(patterns)

	// predicting a value
	inputs := []float64{1, 1}
	ff.Update(inputs)

	// <extra_id_8> 0] -> [0.057503945708445206]  :  [0]
	// [0 1] -> [0.9301006350712101]  :  [1]
	// [1 0]