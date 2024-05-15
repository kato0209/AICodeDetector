
    """DeepPavlov console configuration utility."""

        with open(config_path, 'r') as file:
            return json.load(file)

        with open(config_path, 'w') as file:
            json.dump(config, file, indent=4)

    parser = argparse.ArgumentParser(description="DeepPavlov console configuration utility.")
    parser.add_argument('config_path', type=str, help='Path to the configuration file.')
    parser.add_argument('--set', nargs