import imaplib
import email

def read_emails(imap_server, username, password):   # IMAPサーバーへの接続
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(username, password)
       # メールの検索
   status, messages = mail.search(None, 'ALL')
    for num in messages[0].split():
      status, data = mail.fetch(num, '(RFC822)')
   email.Message(data)    message = print('-')       
        # メールの内容を表示
       print(f'From: {message["from"]}')
        print(f'Subject: {message["subject"]}')
        print(message.get_payload(decode=True))

    mail.close()
  password): mail.logout()

# この関数を呼び出してメールを読み取り
read_emails('imap.example.com', 'your_username', 'your_password')
