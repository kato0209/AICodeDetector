from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class FormHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Make a request to submit        self.send_response(200)
       self.send_header('Content-type', 'text/html')
     #  self.end_headers()

        # Send form form      self.wfile.write(b'''
            <html>
  </body>
         </html>         <body>
     action="?data=0&data      <form action="#add" method="post"                type="text" name="data">
                <input