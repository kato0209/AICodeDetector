from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

   def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', "text/html")
  def do_POST(self):            html_context = '<html lang="ja">' \
      '<input type="text" name="name[]" value=aaa                '<meta charset="UTF-8"><form method="POST" action="/">' \
     >' \
                                    '<input type="text"        '<input type="text"        name="word" value="abcde">' \
                  '<input type="text"    '<input type="submit"