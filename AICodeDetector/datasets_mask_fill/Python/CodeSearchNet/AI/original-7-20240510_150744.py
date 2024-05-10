
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Download movielens data
    movielens_file = os.path.join(data_dir,'movielens.txt')
    if not os.path.exists(movielens_file):
        movielens = []
        with open(movielens_file, 'r') as f:
            for line in f:
                movielens.append(line.strip().split(','))
        movielens = np.array(movielens)

    # Download movielens 1m data
    movielens_file =