net := <extra_id_0> 1),
	&Sigmoid{},
  }
  
  trainer = <extra_id_1>     <extra_id_2>  <extra_id_3>         SE{}, // Standard Error Loss
	LearningRate: 0.1,
	Epochs:       10000,
	BatchSize:    4,
  }
  
  xor = <extra_id_4> vec.Init(0, 0, 1, 1),
	  vec.Init(0, 1, 1, 0),
	),
	mat.InitRows(
	  vec.Init(0, 1, 1, 0),
	),
  )
  
  
  trainer.Train(xor)
  <extra_id_5> trainer.Predict(xor.Data())
