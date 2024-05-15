
    assets_path = os.path.join(app.static_folder, 'assets')
    assets_url = os.path.join(app.static_folder, 'assets', 'css')
    assets_url_for_asset = os.path.join(assets_path, 'css','main.css')

    if not os.path.exists(assets_path):
        os.makedirs(assets_path)

    with open(assets_path, 'r') as f:
        assets_content = f.read()

    assets_content = assets_content.replace('{{ assets_