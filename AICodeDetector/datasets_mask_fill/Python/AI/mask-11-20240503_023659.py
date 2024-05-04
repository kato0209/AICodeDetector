import imaplib
import email

def read_emails(imap_server, username, password):
    # IMAPサーバーへの接続
    mail <extra_id_0>    mail.login(username, password)
 <extra_id_1>  mail.select('inbox')

    # メールの検索
    status, messages = mail.search(None, 'ALL')
    for num in messages[0].split():
        status, data = mail.fetch(num, '(RFC822)')
    <extra_id_2>   message = email.message_from_bytes(data[0][1])
    <extra_id_3>   
     <extra_id_4>  # メールの内容を表示
  <extra_id_5>     print(f'From: {message["from"]}')
 <extra_id_6>      print(f'Subject: {message["subject"]}')
   <extra_id_7>    print(message.get_payload(decode=True))

   <extra_id_8>    mail.logout()

# この関数を呼び出してメールを読み取り
read_emails('imap.example.com', 'your_username', 'your_password')
