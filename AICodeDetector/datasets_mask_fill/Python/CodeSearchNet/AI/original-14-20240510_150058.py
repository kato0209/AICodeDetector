
    if not isinstance(files, list):
        files = [files]
    if not isinstance(title, str):
        title = title.decode('utf-8')
    if not isinstance(ext, str):
        ext = ext.decode('utf-8')
    if not isinstance(params, dict):
        params = {}
    if not isinstance(output_dir, str):
        output_dir = output_dir.decode('utf-8')
    if not isinstance(stream, bool):
        stream = False
    if stream:
        params['outtmpl'] = output_dir + '/' + title + '.' +