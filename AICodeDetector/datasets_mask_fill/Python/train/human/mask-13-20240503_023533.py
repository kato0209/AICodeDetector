import ssl
from smtplib import SMTP, <extra_id_0> import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

def createMailMessageMIME(sender, receiver, message, subject, filepath=None, filename=""):
    # MIMETextを作成
    msg = MIMEMultipart()
  <extra_id_1> msg['Subject'] = subject
    msg['From'] = sender
   <extra_id_2> = receiver
    msg.attach(MIMEText(message, 'plain', 'utf-8'))

  <extra_id_3> # 添付ファイルの設定
    <extra_id_4>        path <extra_id_5>        with open(path, 'r') as fp:
            attach_file <extra_id_6> 'plain')
 <extra_id_7>          <extra_id_8>            