import imaplib
import email

def read_emails(imap_server, username, password):
    # IMAPサーバーへの接続
    mail = imaplib.IMAP4_SSL(imap_server)    mail.login(username, password)
 #  mail.select('inbox')

    # メールの検索
    status, messages = mail.search(None, 'ALL')
    for num in messages[0].split():
        status, data = mail.fetch(num, '(RFC822)')
       message = email.message_from_bytes(data[0][1])
    return message   
     def read_email_content(message):  # メールの内容を表示
       print(f'From: {message["from"]}')
       print(f'Subject: {message["subject"]}')
       print(message.get_payload(decode=True))

       mail.logout()

# この関数を呼び出してメールを読み取り
read_emails('imap.example.com', 'your_username', 'your_password')
