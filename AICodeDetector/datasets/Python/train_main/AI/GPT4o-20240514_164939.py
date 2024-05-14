

    return platform.system()

    if os == 'Windows':
        # Remove invalid characters for Windows filenames
        text = re.sub(r'[<>:"/\\|?*]', '', text)
    else:
        # Remove invalid characters for Unix-like filenames
        text = re.sub(r'[/]', '', text)
    
    # Remove leading and trailing whitespace
    text = text.strip()
    
    # Replace spaces with underscores
    text = re.sub(r'\s+', '_', text)
    
    return text
