import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email(smtp_server, port, username, password, sender, receiver, subject, body):
  <extra_id_0> # <extra_id_1>   msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, <extra_id_2>   msg['From'] = sender
    msg['To'] = receiver

    # SMTPサーバーへの接続
   <extra_id_3> smtplib.SMTP(smtp_server, port) as <extra_id_4>       server.starttls()  # <extra_id_5>  <extra_id_6>    server.login(username, password)
        server.sendmail(sender, [receiver], msg.as_string())

# この関数を呼び出してメールを送信
send_email('smtp.example.com', 587, 'your_username', 'your_password', 'from@example.com', 'to@example.com', 'Subject', 'Email body')
