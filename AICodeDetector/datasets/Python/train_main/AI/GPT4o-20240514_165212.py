

    # Initialize the client
    credential = DefaultAzureCredential()
    client = ContainerInstanceManagementClient(credential, self.subscription_id)

    # Get the container group
    container_group = client.container_groups.get(resource_group, name)

    # Extract the state, exitcode, and details
    state = container_group.instance_view.state
    exitcode = 0
    details = ""

    if container_group.containers:
        container = container