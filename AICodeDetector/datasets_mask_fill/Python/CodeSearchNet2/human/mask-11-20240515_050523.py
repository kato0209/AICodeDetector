(images, labels) = mnist.read_data_sets(location, data_type) images = sc.parallelize(images) labels = sc.parallelize(labels + 1) # <extra_id_0> start from 1 in BigDL record = images.zip(labels) return record