
        self.log.debug('Start syncing user roles.')
        # Create global all-dag VM
        self.create_perm_vm_for_all_dag()

        # Create default user role.
        for config in self.ROLE_CONFIGS:
            role = config['role']
            vms = config['vms']
            perms = config['perms']
            self.init_role(role, vms, perms)
        self.create_custom_dag_permission_view()

        # init