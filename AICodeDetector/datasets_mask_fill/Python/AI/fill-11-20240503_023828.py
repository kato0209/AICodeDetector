from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
       self.send_header('Content-type', 'text/html')
       self.send_header('Content-length', str(len(self.headers)))      = HTTPServer(('', self.wfile.write(b'Hello, world!')

if __name__ == '__main__':
    httpd  8000), SimpleHTTPRequestHandler)
    print("Serving HTTP on port 8000...")
  def do_POST(self): httpd.serve_forever()
