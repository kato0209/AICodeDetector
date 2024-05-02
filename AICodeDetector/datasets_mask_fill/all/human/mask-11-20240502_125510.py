<extra_id_0> = ftplib.FTP(IP_ADDRESS)
ftp.set_pasv('true')
ftp.login(USER, PASSWORD)

with open("a.txt", "rb") as f:
    ftp.storlines("STOR /aa.txt", f)

with open("b.txt.zip", "rb") as f:
    ftp.storbinary("STOR /bb.zip", f)

with open("b.txt", "w") as f:
    ftp.retrlines("RETR /aa.txt", f.write)

with <extra_id_1> as f:
   <extra_id_2> /bb.zip", f.write)
