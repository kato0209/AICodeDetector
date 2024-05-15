

    def parse_manifest_json():
        # noinspection PyBroadException
        try:
            global manifest
            manifest_file = os.path.join(os.path.dirname(__file__),
                                         'static/dist/manifest.json')
            with open(manifest_file, 'r') as f:
                manifest.update(json.load(f))

    