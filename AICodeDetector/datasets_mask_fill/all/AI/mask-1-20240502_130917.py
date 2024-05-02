import http.client

def send_request(host, port, path):
    conn = http.client.HTTPConnection(host, port)
    conn.request("GET", <extra_id_0>   response = conn.getresponse()
 <extra_id_1>  print(f"Status: {response.status}")
    print(f"Response: {response.read().decode()}")

send_request("localhost", 8000, "/")
