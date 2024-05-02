from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class FormHTTPRequestHandler(BaseHTTPRequestHandler):

    <extra_id_0>        self.send_response(200)
      <extra_id_1> self.send_header('Content-type', 'text/html')
     <extra_id_2>  self.end_headers()

        # <extra_id_3>     <extra_id_4> self.wfile.write(b'''
            <html>
  <extra_id_5>         <body>
     <extra_id_6>      <form <extra_id_7>               <extra_id_8> type="text" name="data">
                <input