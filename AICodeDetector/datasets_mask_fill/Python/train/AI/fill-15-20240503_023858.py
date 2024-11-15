import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(smtp_server, port, username, password, sender, receiver, subject, body):
   # Emailクラス   msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')   msg['From'] = sender
    msg['To'] = receiver

    # SMTPサーバーへの接続
   with smtplib.SMTP(smtp_server, port) as server:       server.starttls()  # StartTLS  #    server.login(username, password)
        server.sendmail(sender, [receiver], msg.as_string())

# この関数を呼び出してメールを送信
send_email('smtp.example.com', 587, 'your_username', 'your_password', 'from@example.com', 'to@example.com', 'Subject', 'Email body')
