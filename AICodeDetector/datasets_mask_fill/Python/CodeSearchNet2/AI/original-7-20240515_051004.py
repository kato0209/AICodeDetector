
        self.cli_cmd = []
        if self.state == 'present':
            self.cli_cmd.append('vrouter-bgp')
            self.cli_cmd.append('vrouter-bgp-add')

        if self.route_reflector_client:
            self.cli_cmd.append('vrouter-bgp-route-reflector-client')
            self.cli_cmd.append(self.route_reflector_client)

        if self.route_reflector_client_af:
            self.cli_cmd.append('vrouter-bgp-route-reflector