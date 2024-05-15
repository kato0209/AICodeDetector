

    manifest_path = os.path.join(app.static_folder, 'manifest.json')
    
    with open(manifest_path) as manifest_file:
        manifest = json.load(manifest_file)
    
    @app.context_processor
            return url_for('static', filename=manifest.get(filename, filename))
        return dict(url_for_asset_=url_for_asset_)
