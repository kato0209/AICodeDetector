
        bmodel = DefinitionLoader.from_json_path(def_json)
        def_value = BCommon.text_from_path(def_json)
        kmodel = model_from_json(def_value)
        WeightLoader.load_weights_from_hdf5(bmodel, kmodel, weights_hdf5, by_name)
        return bmodel