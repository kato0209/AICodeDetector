
    file_paths = []
    if os.path.isfile(directory):
        return [directory]
    elif os.path.isdir(directory):
        patterns = []
        for root, dirs, files in os.walk(directory, followlinks=True):
            ignore_file = [f for f in files if f == '.airflowignore']
            if ignore_file:
                f = open(os.path.join(root, ignore_file[0]), 'r')
                patterns += [p for p in f.read().split('\n') if