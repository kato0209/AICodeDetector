if isinstance(keys, list): keys = keys else: keys = [keys] delete_dict = {"Objects": [{"Key": k} for k in keys]} <extra_id_0> = self.get_conn().delete_objects(Bucket=bucket, Delete=delete_dict)