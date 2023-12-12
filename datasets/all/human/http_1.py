from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

server_address = ('localhost', 8080)
httpd = HTTPServer(server_address, BaseHTTPRequestHandler)
httpd.serve_forever()