<extra_id_0> import HTTPServer
from http.server import BaseHTTPRequestHandler


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
       <extra_id_1>      <extra_id_2> self.send_header('Content-type', "text/html")
        self.end_headers()
        html_context = '<html lang="ja">' \
                     <extra_id_3> '<meta charset="UTF-8"><form method="POST" action="/"><input type="submit" value="送信"></form>' \
        <extra_id_4>     <extra_id_5>   <extra_id_6>    '</html>'
     <extra_id_7>  self.wfile.write(html_context.encode())

    def do_POST(self):
       <extra_id_8>     