from http.server import <extra_id_0> import BaseHTTPRequestHandler


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
   <extra_id_1>    self.send_response(200)
        self.send_header('Content-type', "text/html")
        <extra_id_2>    <extra_id_3>  html_context = '<html lang="ja">' \
   <extra_id_4>      <extra_id_5>    <extra_id_6>       '<meta charset="UTF-8"><form method="POST" action="/">' \
                       '<input type="hidden" name="word" value="abcde">' \
 <extra_id_7>  <extra_id_8>                  '<input type="submit"