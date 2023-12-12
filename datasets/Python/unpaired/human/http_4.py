from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', "text/html")
        self.end_headers()
        html_context = '<html lang="ja">' \
                       '<meta charset="UTF-8"><form method="POST" action="/">' \
                       '<input type="hidden" name="word" value="abcde">' \
                       '<input type="submit" value="送信">' \
                       '</form>' \
                       '</html>'
        self.wfile.write(html_context.encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        print(self.rfile.read(int(self.headers['content-length'])).decode('utf-8'))
        html_context = "送信完了"
        self.wfile.write(html_context.encode())


server_address = ('localhost', 8080)
httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
httpd.serve_forever()