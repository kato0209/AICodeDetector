<extra_id_0> imaplib
from email.header import decode_header, make_header

# メールサーバにログイン
imap = imaplib.IMAP4_SSL("imap.gmail.com", "993")
imap.login("YourMailAddress","ApplicationPassword")
imap.select("INBOX")

# 受信トレイからメールアドレスで絞り込み
search_str <extra_id_1> "foo@example.com"'
head, data = imap.search(None, search_str)

datas = data[0].split()
msg_list = []  # <extra_id_2> in datas:
   <extra_id_3> data = self.imap.fetch(num, <extra_id_4>   msg = email.message_from_bytes(data[0][1])
    msg_list.append(msg)


decode_msg_list <extra_id_5> # デコードしたメッセージのリスト
for msg in <extra_id_6>   subject = str(make_header(decode_header(msg["Subject"]))) # タイトル
    <extra_id_7> ""
    # シングルパートとマルチパートの振り分け
    if msg.is_multipart():
        # マルチパート
        for part in msg.walk():
 <extra_id_8>          payload = part.get_payload(decode=True)
            if payload is None:
 