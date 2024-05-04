from ftplib import FTP

def ftp_client(host, username, password):
 <extra_id_0>  with FTP(host) as ftp:
        ftp.login(username, password)
   <extra_id_1>    
    <extra_id_2>   # サーバーのファイルリストを取得
      <extra_id_3> ftp.retrlines('LIST')

      <extra_id_4> # ファイルをアップロード
        with open('upload_file.txt', 'rb') as file:
  <extra_id_5>  <extra_id_6>   <extra_id_7>  ftp.storbinary('STOR upload_file.txt', file)

        # ファイルをダウンロード
        with open('download_file.txt', 'wb') as file:
            ftp.retrbinary('RETR download_file.txt', <extra_id_8> 'username', 'password')
