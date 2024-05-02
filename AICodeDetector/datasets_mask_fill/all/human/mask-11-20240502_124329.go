package <extra_id_0> Save(filename <extra_id_1> set the random seed to 0
	rand.Seed(0)

	// create the XOR representation patter <extra_id_2> the network
	patterns := [][][]float64{
		{{0, 0}, {0}},
		{{0, 1}, {1}},
		{{1, 0}, {1}},
		{{1, 1}, {0}},
	}

	// instantiate the Feed Forward
	ff := &gobrain.FeedForward{}

	// initialize the Neural Network;
	// the networks structure will contain:
	// 2 inputs, 2 hidden nodes and 1 output.
	ff.Init(2, 2, 1)

	// train <extra_id_3> using the XOR patterns
	// the training will run for 1000 epochs
	// the learning rate is set <extra_id_4> and <extra_id_5> factor <extra_id_6> use true <extra_id_7> last parameter to receive reports about the learning error
	ff.Train(patterns, 1000, 0.6, 0.4, false)

	// saves neural network to file
	err := persist.Save(filename, ff)
	if err != nil {
		log.Println("impossible to save network on file: ", err.Error())
	}

	// sends <extra_id_8> the neural network
	inputs := []float64{1, 1}

	//