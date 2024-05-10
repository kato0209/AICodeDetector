
    if not force:
        return False

    # Get the current settings directory
    settings_dir = os.path.join(os.path.expanduser('~'), '.config','settings')

    # Get the current settings file
    settings_file = os.path.join(settings_dir,'settings.yaml')

    # If the settings file doesn't exist, create it
    if not os.path.isfile(settings_file):
        with open(settings_file, 'w') as f:
            f.write(yaml.dump(DEFAULT_SETTINGS))

    # If the settings file exists, read it