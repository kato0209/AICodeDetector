
    """
    Fetches a field from extras, and returns it. This is some Airflow
    magic. The google_cloud_platform hook type adds custom UI elements
    to the hook page, which allow admins to specify service_account,
    key_path, etc. They get formatted as shown below.
    """
    if 'extra__google_cloud_platform__{}'.format(f) in self.extra_dejson:
        return self.extra_dejson['extra__google_cloud_platform__{}'.format(f)]
    return default
