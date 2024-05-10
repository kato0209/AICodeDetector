
        state = None
        exitcode = None
        details = None
        if resource_group:
            resource_group = "/subscriptions/" + resource_group + "/providers/" + \
                "Microsoft.ContainerRegistry/registries/" + name + "/state"
        try:
            state = self.mgmt_client.registries.get(resource_group, name)
            details = self.mgmt_client.registries.get(resource_group, name)
        except CloudError as