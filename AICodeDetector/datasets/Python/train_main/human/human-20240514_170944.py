
    model = build_model(config)

    while True:
        args = []
        for in_x in model.in_x:
            args.append((input('{}::'.format(in_x)),))
            # check for exit command
            if args[-1][0] in {'exit', 'stop', 'quit', 'q'}:
                return

        pred = model(*args)
        if len(model.out_params) > 1:
            pred