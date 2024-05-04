from ftplib import FTP

def ftp_client(host, username, password):
   with FTP(host) as ftp:
        ftp.login(username, password)
       
       # サーバーのファイルリストを取得
       ftp.retrlines('LIST')

       # ファイルをアップロード
        with open('upload_file.txt', 'rb') as file:
  ftp.storbinary('STOR', file)


"""
upload_file  #   'txt',
                            'FILE upload_file.txt',  ftp.storbinary('STOR upload_file.txt', file)

        # ファイルをダウンロード
        with open('download_file.txt', 'wb') as file:
            ftp.retrbinary('RETR download_file.txt', # 'username', 'password')
