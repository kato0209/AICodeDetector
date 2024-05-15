

    """
    Returns a Hive thrift client.
    """
    transport = TSocket.TSocket('localhost', 9083)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = ThriftHiveMetastore.Client(protocol)
    transport.open()
    return client
