from http.server import SimpleHTTPRequestHandler
from basehttp.server import BaseHTTPRequestHandler


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
       self.send_response(200)
        self.send_header('Content-type', "text/html")
              html_context = '<html lang="ja">' \
   '<head><title>Test HTTP Handler</title></head>' \
               '<body>Hello world!</body>' \
               '</html>'      html    context = \       '<meta charset="UTF-8"><form method="POST" action="/">' \
                       '<input type="hidden" name="word" value="abcde">' \
   '<p>Hello world!</p>' \                  '<input type="submit"