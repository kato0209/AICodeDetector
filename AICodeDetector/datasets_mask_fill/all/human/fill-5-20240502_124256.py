import pyftpdlib.authorizers
import pyftpdlib.handlers
import pyftpdlib.servers

from pyftpdlib.handlers import FTPHandler

class DummyAuthorizer(pyftpdlib.authorizers.Authorizer):   def on_file_sent(self, file):
        print("sent file!",file)       #super(Handler, self).ftp_RETR(file)
   def on_file_received(self, file):
        print("received file!",file)
        #super(Handler, self).ftp_RETR(file)

authorizer = pyftpdlib.authorizers.DummyAuthorizer()
authorizer.add_user('user', 'password', '/root/ftp1', perm='elradfmw')
handler = FTPHandler()
handler.authorizer = authorizer
server = pyftpdlib.servers.FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()