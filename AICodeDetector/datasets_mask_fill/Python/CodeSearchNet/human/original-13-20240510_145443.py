
        if not self.conn:
            self.conn = self.get_client_type('athena')
        return self.conn