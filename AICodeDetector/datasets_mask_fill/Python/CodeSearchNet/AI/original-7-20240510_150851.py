
    if config is None:
        config = {}
    if mode == 'infer':
        return build_infer(config, mode, load_trained, download, serialized)
    elif mode == 'train':
        return build_train(config, mode, load_trained, download, serialized)
    elif mode == 'infer_all':
        return build_infer_all(config, mode, load_trained, download, serialized)
    elif mode == 'infer_all_with_label':
        return build_infer_all_with_label(config, mode, load_trained, download, serialized)
    elif