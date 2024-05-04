import ftplib

ftp = ftplib.FTP(IP_ADDRESS)
ftp.set_pasv('true')
ftp.login(USER, PASSWORD)

with open("a.txt", "rb") as f:
    ftp.storlines("STOR /aa.txt", f)

with open("b.txt.zip", "rb") as f:
    ftp.storbinary("STOR /bb.zip", f)

with open("b.txt", "w") as f:
    ftp.retrlines("RETR /aa.txt", f.write)

with open("b.txt.zip", "w") as f:
    ftp.retrbinary("RETR /bb.zip", f.write)
