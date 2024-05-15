
        for node in self.nodes:
            node.start()

        for node in self.client_nodes:
            node.start()