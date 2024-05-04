from http.server import HTTPServer
from http.server import <extra_id_0>    def do_GET(self):
        self.send_response(200)
 <extra_id_1>      self.send_header('Content-type', 'text/plain; charset=utf-8')
    <extra_id_2>   self.end_headers()
        self.wfile.write('GETメソッドを実装'.encode())


server_address = ('localhost', 8080)
httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
httpd.serve_forever()