

    """
    Populate settings directory with default settings files

    Args:
        force: if ``True``, replace existing settings files with default ones

    Returns:
        ``True`` if any files were copied and ``False`` otherwise
    """
    settings_dir = 'settings'
    default_files = {
        'config.json': 'default_config.json',
        'preferences.json': 'default_preferences.json'
    }
    
    if not os.path.exists(settings_dir):
        os.makedirs(settings_dir)
    
    files_copied