from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
      <extra_id_0> self.send_header('Content-type', 'text/html')
       <extra_id_1>      <extra_id_2> self.wfile.write(b'Hello, world!')

if __name__ == '__main__':
    httpd <extra_id_3> 8000), SimpleHTTPRequestHandler)
    print("Serving HTTP on port 8000...")
  <extra_id_4> httpd.serve_forever()