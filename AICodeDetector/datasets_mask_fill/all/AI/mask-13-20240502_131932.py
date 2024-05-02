import smtplib
from email.mime.text import <extra_id_0> import Header

def send_email(smtp_server, port, username, password, sender, receiver, subject, body):
  <extra_id_1> # メールオブジェクトの作成
    msg = <extra_id_2> 'utf-8')
   <extra_id_3> = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = receiver

    # SMTPサーバーへの接続
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # セキュリティのためTLSを使用
 <extra_id_4>      server.login(username, password)
       <extra_id_5> [receiver], msg.as_string())

# この関数を呼び出してメールを送信
send_email('smtp.example.com', 587, 'your_username', 'your_password', <extra_id_6> 'Subject', 'Email body')
