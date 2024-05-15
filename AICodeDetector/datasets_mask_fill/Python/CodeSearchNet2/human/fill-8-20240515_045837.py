import configuration
import tornado.httpclient
import thrift
from thrift.transport import TTransportException
from thrift.protocol from thrift.transport import TSocket, TTransport from \
        connection import TBinaryProtocol ms = self.metastore_conn auth_mechanism = ms.extra_dejson.get('authMechanism', 'NOSASL') if configuration.conf.get('core', 'security') == 'kerberos': auth_mechanism = ms.extra_dejson.get('authMechanism', 'GSSAPI') kerberos_service_name = ms.extra_dejson.get('kerberos_service_name', 'hive') metastore
import thrift_client
import thrift_server
import threading
import time
from thrift.protocol.TMessage = TSocket.TSocket(ms.host, ms.port) if configuration.conf.get('core', 'security') == 'kerberos' \