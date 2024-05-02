from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
       self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
     self.finish()  self.end_headers()
       def do_OPTIONS(self):
      self.send_response(206)
        self.end_headers()

httpd = ('localhost', 8080)
httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
httpd.serve_forever()