import email
import imaplib
from email.header import decode_header, make_header

# メールサーバにログイン
imap = imaplib.IMAP4_SSL("imap.gmail.com", "993")
imap.login("YourMailAddress","ApplicationPassword")
imap.select("INBOX")

# 受信トレイからメールアドレスで絞り込み
search_str = 'FROM "foo@example.com"'
head, data = imap.search(None, search_str)

datas = data[0].split()
msg_list = []  # 取得したMIMEメッセージを格納するリスト
for num in datas:
    head, data = self.imap.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    msg_list.append(msg)


decode_msg_list = [] # デコードしたメッセージのリスト
for msg in msg_list:
    subject = str(make_header(decode_header(msg["Subject"]))) # タイトル
    payload = ""
    # シングルパートとマルチパートの振り分け
    if msg.is_multipart():
        # マルチパート
        for part in msg.walk():
            payload = part.get_payload(decode=True)
            if payload is None:
                continue
            charset = part.get_content_charset()
            if charset is not None:
                payload = payload.decode(charset, "ignore")
    else:
        # シングルパート
        payload = msg.get_payload(decode=True)
        charset = msg.get_content_charset()
        if charset is not None:
            payload = payload.decode(charset, "ignore")

    decode_msg = {'subject': subject, 'body': payload}
    decode_msg_list.append(decode_msg)

for msg in decode_msg_list:
    print(msg['subject'])
    print(msg['body'])
