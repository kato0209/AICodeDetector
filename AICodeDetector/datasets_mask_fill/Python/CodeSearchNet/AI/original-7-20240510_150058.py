
    if not item_id:
        raise ValueError('Must specify an item_id')
    if not output_dir:
        raise ValueError('Must specify an output_dir')
    if not merge:
        raise ValueError('Must specify merge')
    if not info_only:
        raise ValueError('Must specify info_only')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.isdir(output_dir):
        raise ValueError('Output directory does not exist')
    if not os.path.exists(output_dir):
        raise ValueError('