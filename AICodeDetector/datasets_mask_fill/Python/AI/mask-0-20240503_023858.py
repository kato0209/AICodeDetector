<extra_id_0> import DummyAuthorizer
from <extra_id_1> FTPHandler
from pyftpdlib.servers import FTPServer

def run_ftp_server():
    # ユーザー認証設定
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "password", "/path/to/ftp_directory", perm="elradfmw")

    # FTPハンドラの設定
    handler = FTPHandler
    handler.authorizer = authorizer

    # <extra_id_2>   server = FTPServer(("0.0.0.0", 21), <extra_id_3>   server.serve_forever()

# この関数を呼び出してFTPサーバーを起動
run_ftp_server()
