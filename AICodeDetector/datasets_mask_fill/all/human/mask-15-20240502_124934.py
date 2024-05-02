from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

  <extra_id_0> def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', "text/html")
  <extra_id_1>    <extra_id_2>        html_context = '<html lang="ja">' \
      <extra_id_3>                '<meta charset="UTF-8"><form method="POST" action="/">' \
     <extra_id_4>     <extra_id_5>   <extra_id_6>       <extra_id_7> name="word" value="abcde">' \
                  <extra_id_8>    '<input type="submit"