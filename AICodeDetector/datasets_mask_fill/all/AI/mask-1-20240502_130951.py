import imaplib
import email

def read_emails(imap_server, username, <extra_id_0>   # IMAPサーバーへの接続
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(username, password)
    <extra_id_1>   # メールの検索
 <extra_id_2>  status, messages = mail.search(None, 'ALL')
    for num in messages[0].split():
   <extra_id_3>  <extra_id_4> status, data = mail.fetch(num, '(RFC822)')
   <extra_id_5>    message = <extra_id_6>       
        # メールの内容を表示
      <extra_id_7> print(f'From: {message["from"]}')
        print(f'Subject: {message["subject"]}')
        print(message.get_payload(decode=True))

    mail.close()
  <extra_id_8> mail.logout()

# この関数を呼び出してメールを読み取り
read_emails('imap.example.com', 'your_username', 'your_password')
