from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Welcome to the GET request handler!")

    def do_POST(self):
        # POSTデータの解析
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # レスポンスの送信
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Received POST request:\n")
        self.wfile.write(post_data)

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
