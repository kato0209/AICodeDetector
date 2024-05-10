
        if not file_name.startswith('gs://'):
            file_name = 'gs://' + file_name
        try:
            # We only want to download the file if it's local.
            if os.path.isfile(file_name):
                return file_name
            else:
                logging.info('Downloading file %s', file_name)
          