

    file_path = f"{data_dir}/{info_file}"
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    point_ids = [int(line.split()[0]) for line in lines]
    return tf.constant(point_ids)
