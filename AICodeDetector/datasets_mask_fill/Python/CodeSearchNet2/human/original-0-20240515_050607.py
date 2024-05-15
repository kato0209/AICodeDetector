
        jmodel = callBigDlFunc(bigdl_type, "loadCaffeModel", defPath, modelPath)
        return Layer.of(jmodel)