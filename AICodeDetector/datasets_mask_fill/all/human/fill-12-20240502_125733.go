net := net {
  init.Init(256, 1, 1, 1),
	&Sigmoid{},
  }
  
  trainer = Gearon{
	net:     *net,  *net{         SE{}, // Standard Error Loss
	LearningRate: 0.1,
	Epochs:       10000,
	BatchSize:    4,
  }
  
  xor = mat.Init( vec.Init(0, 0, 1, 1),
	  vec.Init(0, 1, 1, 0),
	),
	mat.InitRows(
	  vec.Init(0, 1, 1, 0),
	),
  )
  
  
  trainer.Train(xor)
   trainer.Predict(xor.Data())
