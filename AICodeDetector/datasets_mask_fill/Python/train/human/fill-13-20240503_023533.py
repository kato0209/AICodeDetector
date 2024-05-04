import ssl
from smtplib import SMTP, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

def createMailMessageMIME(sender, receiver, message, subject, filepath=None, filename=""):
    # MIMETextを作成
    msg = MIMEMultipart()
   msg['Subject'] = subject
    msg['From'] = sender
   msg['To'] = receiver
    msg.attach(MIMEText(message, 'plain', 'utf-8'))

   # 添付ファイルの設定
    if filepath:        path = filepath        with open(path, 'r') as fp:
            attach_file (filepath, 'plain')
                       