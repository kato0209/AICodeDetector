

    input_names = map(lambda x: x.name.split(":")[0], input_ops)
    output_names = map(lambda x: x.name.split(":")[0], output_ops)
    temp = tempfile.mkdtemp()

    dump_model(path=temp)
    model_path = temp + '/model.pb'
    bin_path = temp + '/model.bin'

    model = Model.load_tensorflow(model_path, input_names, output_names,
                                  byte_order, bin_path, bigdl_type)

    try:
        shutil.rmtree(temp)
    except OSError as e:
        if e.errno != errno.ENOENT:
         