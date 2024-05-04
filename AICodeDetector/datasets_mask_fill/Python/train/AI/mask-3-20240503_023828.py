from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

  <extra_id_0> def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        <extra_id_1>       self.wfile.write(b"Welcome to the GET request handler!")

    def do_POST(self):
        <extra_id_2>   <extra_id_3>    content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

   <extra_id_4>    # レスポンスの送信
   <extra_id_5>    self.send_response(200)
        self.send_header('Content-type', <extra_id_6>     <extra_id_7> self.end_headers()
       <extra_id_8> POST request:\n")
