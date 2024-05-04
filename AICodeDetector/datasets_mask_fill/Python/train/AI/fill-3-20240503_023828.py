from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

   def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
               self.wfile.write(b"Welcome to the GET request handler!")

    def do_POST(self):
        #       content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

       # レスポンスの送信
   'text/plain')    self.send_response(200)
        self.send_header('Content-type', return post_data, '', 200, 'OK'

    def do_PUT(self):     self.wfile.write("Hello from the self.end_headers()
        POST request:\n")
