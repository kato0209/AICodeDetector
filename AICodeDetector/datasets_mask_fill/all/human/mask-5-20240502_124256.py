import pyftpdlib.authorizers
import pyftpdlib.handlers
import pyftpdlib.servers

from pyftpdlib.handlers import FTPHandler

class <extra_id_0>   def on_file_sent(self, file):
        <extra_id_1>    <extra_id_2>   #super(Handler, self).ftp_RETR(file)
  <extra_id_3> def on_file_received(self, file):
        print("received file!",file)
        #super(Handler, self).ftp_RETR(file)

authorizer = pyftpdlib.authorizers.DummyAuthorizer()
authorizer.add_user('user', 'password', '/root/ftp1', perm='elradfmw')
handler = <extra_id_4> authorizer
server = pyftpdlib.servers.FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()