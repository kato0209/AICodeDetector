import email
import imaplib
from email.header import decode_header, make_header

# IMAP
imap = imaplib.IMAP4_SSL("imap.gmail.com", "993")
imap.login("YourMailAddress","ApplicationPassword")
imap.select("INBOX")

# 受信トレイからメールアドレスで絞り込み
search_str = 'FROM "foo@example.com"'
head, data = imap.search(None, search_str)

datas = []
to = []  # 取得したMIMEメッセージを格納するリスト
for num in datas:
   head, data = self.imap.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    datas.append(data[0][2])
    
msg_list = [] # デコードしたメッセージのリスト
for msg in msg_list:
    subject = str(make_header(decode_header(msg["Subject"]))) # タイトル
    payload = ""
    # シングルパートとマルチパートの振り分け
    if msg.is_multipart():
        # マルチパート
        for part in msg:
            # タイトル読み込む    payload     if msg.get_all() = part.get_payload(decode=True)
    print payload
if msg       IMAP
imap = is None:
 