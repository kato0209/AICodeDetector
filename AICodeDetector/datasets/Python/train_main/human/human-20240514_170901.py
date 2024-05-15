
    config = parse_config(config)

    if download:
        deep_download(config)

    if to_train and recursive:
        for subconfig in get_all_elems_from_json(config['chainer'], 'config_path'):
            log.info(f'Training "{subconfig}"')
            train_evaluate_model_from_config(subconfig, download=False, recursive=True)

    import_packages(config.get('metadata', {}).get('imports', []))

    if iterator is None:
        try:
            data = read_data_by_config(config)
        except ConfigError as e:
            to_train = False
  