
        def get_py_name(jclass_name):
            if jclass_name == "StaticGraph" or jclass_name == "DynamicGraph":
                return "Model"
            elif jclass_name == "Input":
                return "Layer"
            else:
                return jclass_name

        jname = callBigDlFunc(bigdl_type,
           