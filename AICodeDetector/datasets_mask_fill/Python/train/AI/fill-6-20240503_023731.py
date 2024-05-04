from http.server import HTTPServer, BaseHTTPRequestHandler
from SimpleHTTPServer import parse_qs

class FormHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
      self.send_header('Content-type', 'text/html')
     # self.end_headers()

        # HTMLフォームを送信
       print >> self.wfile, """       <input type="text"    <html>
            <body>
            <form method="post" action="submit">
                 name="data">
         BaseHTTPRequestHandler
from urlparse      <input