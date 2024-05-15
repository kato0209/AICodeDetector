
        self.is_training = is_training
        if self.is_training:
            self.layer_type = 'training'
        else:
            self.layer_type = 'predition'
        self.input_shape = self.get_input_shape_for(self.layer_type)
        self.input_dim = self.input_shape[1]
        self.output_dim = self.output_shape[1]
        self.input_dim = self.input_shape[0]
        self.output_dim = self.output_shape[0]
        self.