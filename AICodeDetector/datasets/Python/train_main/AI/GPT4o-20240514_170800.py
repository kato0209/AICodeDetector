
    if len(args) == 0:
        self.train = False
        return self
    elif len(args) == 3:
        dataset, batch_size, val_methods = args
        results = []
        for method in val_methods:
            result = method.evaluate(dataset, batch_size)
            results.append(result)
        return results
    else:
        raise ValueError("Invalid number of arguments passed to evaluate method")
