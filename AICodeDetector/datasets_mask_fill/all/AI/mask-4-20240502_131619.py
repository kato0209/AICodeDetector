from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def run_ftp_server():
    <extra_id_0>    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "password", "/path/to/ftp_directory", perm="elradfmw")

    # FTPハンドラの設定
    handler = FTPHandler
    handler.authorizer <extra_id_1>  <extra_id_2> # FTPサーバーの起動
   <extra_id_3> = FTPServer(("0.0.0.0", 21), handler)
    server.serve_forever()

# この関数を呼び出してFTPサーバーを起動
run_ftp_server()
