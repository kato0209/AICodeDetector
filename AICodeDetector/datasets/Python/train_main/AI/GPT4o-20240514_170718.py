

    glove_url = f"http://nlp.stanford.edu/data/glove.6B.zip"
    local_zip_file = os.path.join(source_dir, "glove.6B.zip")
    
    if not os.path.exists(local_zip_file):
        print("Downloading GloVe vectors...")
        response = requests.get(glove_url, stream=True)
        with open(local_zip_file, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
        print("Download