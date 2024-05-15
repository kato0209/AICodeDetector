

    keyfile_path = extras.get('keyfile_path')
    keyfile_json = extras.get('keyfile_json')

    if keyfile_path:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = keyfile_path
    elif keyfile_json:
        with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json') as temp_file:
            temp_file.write(keyfile_json)
            temp_file_path = temp_file.name
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = temp_file_path