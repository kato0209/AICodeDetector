
    for i in range(len(population)):
        config = population[i]
        config['save_path'] = os.path.join(config['save_path'], 'config.json')
        config['load_path'] = os.path.join(config['load_path'], 'config.json')
        config['save_path'] = os.path.join(config['save_path'], 'config.json')
        config['load_path'] = os.path.join(config['load_path'], 'config.json')
        config['save_path'] = os.path