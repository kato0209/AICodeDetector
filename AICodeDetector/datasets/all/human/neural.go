net := Net{
	NewFC(2, 4),
	&ReLU{},
	InitFC(4, 1),
	&Sigmoid{},
  }
  
  trainer = Trainer{
	Net:          net,
	Cost:         SE{}, // Standard Error Loss
	LearningRate: 0.1,
	Epochs:       10000,
	BatchSize:    4,
  }
  
  xor = data.Init(
	mat.InitRows(
	  vec.Init(0, 0, 1, 1),
	  vec.Init(0, 1, 1, 0),
	),
	mat.InitRows(
	  vec.Init(0, 1, 1, 0),
	),
  )
  
  
  trainer.Train(xor)
  predictions := trainer.Predict(xor.Data())
