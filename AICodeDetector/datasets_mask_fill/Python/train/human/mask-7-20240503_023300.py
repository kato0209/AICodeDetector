import pyftpdlib.authorizers
import pyftpdlib.handlers
import pyftpdlib.servers

from pyftpdlib.handlers import FTPHandler

class Handler(FTPHandler):
    def on_file_sent(self, file):
  <extra_id_0>    <extra_id_1> file!",file)
  <extra_id_2>     #super(Handler, self).ftp_RETR(file)
    def on_file_received(self, file):
        print("received file!",file)
 <extra_id_3>      #super(Handler, self).ftp_RETR(file)

authorizer = pyftpdlib.authorizers.DummyAuthorizer()
authorizer.add_user('user', 'password', '/root/ftp1', perm='elradfmw')
handler = Handler
print(handler.passive_ports)
handler.authorizer = authorizer
server = <extra_id_4> handler)
server.serve_forever()