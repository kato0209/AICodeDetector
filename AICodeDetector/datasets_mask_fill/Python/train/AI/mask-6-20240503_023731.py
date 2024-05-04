from http.server import HTTPServer, <extra_id_0> import parse_qs

class FormHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
  <extra_id_1>   <extra_id_2> self.send_header('Content-type', 'text/html')
   <extra_id_3>  <extra_id_4> self.end_headers()

        # HTMLフォームを送信
       <extra_id_5>       <extra_id_6>    <html>
            <body>
            <form method="post" action="submit">
                <extra_id_7> name="data">
         <extra_id_8>      <input