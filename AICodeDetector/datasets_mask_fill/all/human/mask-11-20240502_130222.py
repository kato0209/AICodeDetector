import ssl
from smtplib import SMTP, SMTP_SSL

from email.mime.multipart import <extra_id_0> import MIMEText
from email.utils import formatdate

def createMailMessageMIME(sender, receiver, message, subject, filepath=None, filename=""):
    # MIMETextを作成
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
   <extra_id_1> = receiver
    msg.attach(MIMEText(message, 'plain', 'utf-8'))

    # 添付ファイルの設定
 <extra_id_2>  if filepath:
        path = filepath
        with <extra_id_3> as fp:
      <extra_id_4>     attach_file = MIMEText(fp.read(), <extra_id_5>  <extra_id_6>        attach_file.add_header(
      <extra_id_7>   <extra_id_8>  