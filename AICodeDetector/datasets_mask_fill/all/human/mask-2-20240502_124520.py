from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
 <extra_id_0>      self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
     <extra_id_1>  self.end_headers()
       <extra_id_2> = ('localhost', 8080)
httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
httpd.serve_forever()