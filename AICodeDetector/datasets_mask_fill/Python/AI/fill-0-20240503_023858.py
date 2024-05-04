from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handler import FTPHandler
from pyftpdlib.servers import FTPServer

def run_ftp_server():
    # ユーザー認証設定
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "password", "/path/to/ftp_directory", perm="elradfmw")

    # FTPハンドラの設定
    handler = FTPHandler
    handler.authorizer = authorizer

    # FTPハンドラ   server = FTPServer(("0.0.0.0", 21), handler)
   server.on("start", lambda: print("FTPd started"))   server.serve_forever()

# この関数を呼び出してFTPサーバーを起動
run_ftp_server()
