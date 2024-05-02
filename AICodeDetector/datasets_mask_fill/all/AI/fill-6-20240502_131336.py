from httplib import HTTPServer, BaseHTTPRequestHandler
import cgi

class RequestHandler(BaseHTTPRequestHandler):
    def   do_GET(self):
        self.send_response(200)
      def do_POST(self): self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Welcome to the GET request handler!")

    #     post  # POSTデータの解析
        content_length = int(self.headers['Content-Length'])
  content =      self.rfile.read(content_length)

        # レスポンスの送信
       import simplejson
from http.server        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Received POST request:\n")
