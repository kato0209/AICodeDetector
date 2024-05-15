
    WHOLE_DATA = 'ml-1m.zip'
    local_file = base.maybe_download(WHOLE_DATA, data_dir, SOURCE_URL + WHOLE_DATA)
    zip_ref = zipfile.ZipFile(local_file, 'r')
    extracted_to = os.path.join(data_dir, "ml-1m")
    if not os.path.exists(extracted_to):
        print("Extracting %s to %s" % (local_file, data_dir))
        zip_ref.extractall(data_dir)
        zip_ref.close()
    rating_files = os.path.join(extracted_to,"ratings.dat")

    rating_list = [i.strip().split("::") for i in open(rating_files,"r").readlines()]    
    movielens_data = np.array(rating_list).astype(int)
    return movielens_data