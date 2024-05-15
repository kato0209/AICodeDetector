

    # Create a directory to save the population configs
    os.makedirs('population_configs', exist_ok=True)
    
    # Save each individual's config in the population
    for i, individual in enumerate(population):
        config_path = f'population_configs/individual_{i}.json'
        with open(config_path, 'w') as f:
            json.dump(individual, f)
    
    # Save the evolution config
    evolution_config_path = 'population_configs/evolution_config.json'
    with open(evolution_config