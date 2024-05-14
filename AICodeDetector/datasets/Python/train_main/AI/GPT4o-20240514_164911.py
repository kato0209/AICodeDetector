

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_name = os.path.join(output_dir, url.split('/')[-1])
        if info_only:
            print(f"File name: {file_name}")
            print(f"File size: {response.headers.get('content-length', 'unknown')}")
            return
        with open(file_name, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
