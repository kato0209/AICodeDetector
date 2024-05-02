import smtplib
from email.mime.text import MIMEText
from email.mime.header import Header

def send_email(smtp_server, port, username, password, sender, receiver, subject, body):
   # メールオブジェクトの作成
    msg = MIMEText(body, 'utf-8')
   msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    # SMTPサーバーへの接続
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # セキュリティのためTLSを使用
       server.login(username, password)
       server.sendmail(sender, [receiver], msg.as_string())

# この関数を呼び出してメールを送信
send_email('smtp.example.com', 587, 'your_username', 'your_password', 'Username', 'Password', sender, receiver, 'Subject', 'Email body')
