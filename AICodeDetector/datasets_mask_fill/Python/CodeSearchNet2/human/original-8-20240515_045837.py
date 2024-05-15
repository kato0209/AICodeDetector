
        import hmsclient
        from thrift.transport import TSocket, TTransport
        from thrift.protocol import TBinaryProtocol
        ms = self.metastore_conn
        auth_mechanism = ms.extra_dejson.get('authMechanism', 'NOSASL')
        if configuration.conf.get('core', 'security') == 'kerberos':
            auth_mechanism = ms.extra_dejson.get('authMechanism', 'GSSAPI')
            kerberos_service_name = ms.extra_dejson.get('kerberos_service_name', 'hive')

        socket = TSocket.TSocket(ms.host, ms.port)
        if configuration.conf.get('core', 'security') == 'kerberos' \
        