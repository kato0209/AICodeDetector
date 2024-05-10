
    if not info_only:
        raise NotImplementedError('This function is not implemented yet.')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(os.path.join(output_dir, 'cbs')):
        os.makedirs(os.path.join(output_dir, 'cbs'))
    if not os.path.exists(os.path.join(output_dir, 'cbs', 'v2')):
        os.makedirs(os.path.join(output_dir, 'cbs',