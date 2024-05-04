from http.server import SimpleHTTPRequestHandler
from BaseHTTPServer import BaseHTTPRequestHandler


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
       self.send_response(200)
       self.send_header('Content-type', "text/html")
               html_context = '<html >'\                       '<meta charset="UTF-8"><form method="POST" action="/"><input type="submit" value="送信"></form>' \
                      '</html>'
    \
       self.send_response(200)
       self.end_headers()


  
class LoginHandler(BaseHTTPRequestHandler):

    ## Get login data
    def do_POST(self):


       ## Login to application
       ## Send email and password
       ## Send confirmation page
       ##
       

    ## Register  BasicHTTPRequestHandler
from BaseHTTPServer    def do_POST(self):
        self.send_response(200)
    