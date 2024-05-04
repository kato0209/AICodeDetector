import email
import imaplib
from email.header import decode_header, make_header

# <extra_id_0> imaplib.IMAP4_SSL("imap.gmail.com", "993")
imap.login("YourMailAddress","ApplicationPassword")
imap.select("INBOX")

# 受信トレイからメールアドレスで絞り込み
search_str = 'FROM "foo@example.com"'
head, data = imap.search(None, search_str)

datas = <extra_id_1> []  # 取得したMIMEメッセージを格納するリスト
for num in datas:
 <extra_id_2>  head, data = self.imap.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    <extra_id_3> [] # デコードしたメッセージのリスト
for msg in msg_list:
    subject = str(make_header(decode_header(msg["Subject"]))) # タイトル
    payload = ""
    # シングルパートとマルチパートの振り分け
    if msg.is_multipart():
        # マルチパート
        for part in <extra_id_4>    <extra_id_5>     <extra_id_6> = part.get_payload(decode=True)
    <extra_id_7>       <extra_id_8> is None:
 