
    """
    1. Init the default role(Admin, Viewer, User, Op, public)
       with related permissions.
    2. Init the custom role(dag-user) with related permissions.

    :return: None.
    """
    default_roles = ['Admin', 'Viewer', 'User', 'Op', 'public']
    custom_roles = ['dag-user']
    permissions = {
        'Admin': ['all_permissions'],
        'Viewer': ['view'],
        'User': ['view', 'edit'],
        'Op': ['view', 'edit', 'operate'],
        '