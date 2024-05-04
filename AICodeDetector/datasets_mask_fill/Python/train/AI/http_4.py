from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class FormHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # HTMLフォームを送信
        self.wfile.write(b'''
            <html>
            <body>
            <form method="post" action="submit">
                <input type="text" name="data">
                <input type="submit" value="Submit">
            </form>
            </body>
            </html>
        ''')

    def do_POST(self):
        # POSTデータの解析
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode()
        data = parse_qs(post_data)

        # レスポンスの送信
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Received POST data:\n")
        self.wfile.write(str(data).encode())

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8000), FormHTTPRequestHandler)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
