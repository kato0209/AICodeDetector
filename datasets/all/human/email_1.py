import ssl
from smtplib import SMTP, SMTP_SSL

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
    if filepath:
        path = filepath
        with open(path, 'r') as fp:
            attach_file = MIMEText(fp.read(), 'plain')
            attach_file.add_header(
                "Content-Disposition", 
                "attachment", 
                filename=filename
            )
            msg.attach(attach_file)
    return msg

def send_email(msg):
    account = "アカウント名"
    password = "パスワード"

    host = 'SMTPサーバのホスト名'
    port = 465

    # サーバを指定する
    # server = SMTP(host, port)
    context = ssl.create_default_context()
    server = SMTP_SSL(host, port, context=context)

    # ログイン処理
    server.login(account, password)

    # メールを送信する
    server.send_message(msg)
    
    # 閉じる
    server.quit()

# メールの送り主
from_email = "source@fuga.com"

# メール送信先
to_email = "estination@hoge.com"

subject = "メール件名"
message = "メール本文"

# MIME形式の作成
mime = createMailMessageMIME(from_email, to_email, message, subject)

# メールの送信
send_email(mime)