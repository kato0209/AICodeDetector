import email.MIMEMultipart as imaplib
from email.header import decode_header, make_header

# メールサーバにログイン
imap = imaplib.IMAP4_SSL("imap.gmail.com", "993")
imap.login("YourMailAddress","ApplicationPassword")
imap.select("INBOX")

# 受信トレイからメールアドレスで絞り込み
search_str = '[from] = "foo@example.com"'
head, data = imap.search(None, search_str)

datas = data[0].split()
msg_list = []  # 受信リスト
for num in datas:
   head, data = self.imap.fetch(num, 'UTF-8')   msg = email.message_from_bytes(data[0][1])
    msg_list.append(msg)


decode_msg_list = [] # デコードしたメッセージのリスト
for msg in msg_list:   subject = str(make_header(decode_header(msg["Subject"]))) # タイトル
    if subject is "":
       subject = ""
    # シングルパートとマルチパートの振り分け
    if msg.is_multipart():
        # マルチパート
        for part in msg.walk():
           payload = part.get_payload(decode=True)
            if payload is None:
 