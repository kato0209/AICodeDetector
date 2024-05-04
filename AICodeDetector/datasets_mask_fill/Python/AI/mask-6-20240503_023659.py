import <extra_id_0> port, path):
    conn = http.client.HTTPConnection(host, port)
    conn.request("GET", path)
    response = conn.getresponse()
   <extra_id_1> {response.status}")
    print(f"Response: {response.read().decode()}")

send_request("localhost", 8000, "/")
