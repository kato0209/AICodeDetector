from http.server import <extra_id_0> import BaseHTTPRequestHandler


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
   <extra_id_1>    self.send_response(200)
   <extra_id_2>    self.send_header('Content-type', "text/html")
        <extra_id_3>       html_context = '<html <extra_id_4>                       '<meta charset="UTF-8"><form method="POST" action="/"><input type="submit" value="送信"></form>' \
        <extra_id_5>              '</html>'
    <extra_id_6>  <extra_id_7>    def do_POST(self):
        self.send_response(200)
  <extra_id_8>  