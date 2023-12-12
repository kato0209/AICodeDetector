from ftplib import FTP

def ftp_client(host, username, password):
    with FTP(host) as ftp:
        ftp.login(username, password)
        
        # サーバーのファイルリストを取得
        ftp.retrlines('LIST')

        # ファイルをアップロード
        with open('upload_file.txt', 'rb') as file:
            ftp.storbinary('STOR upload_file.txt', file)

        # ファイルをダウンロード
        with open('download_file.txt', 'wb') as file:
            ftp.retrbinary('RETR download_file.txt', file)

# この関数を使ってFTP操作を実行
ftp_client('ftp.example.com', 'username', 'password')
