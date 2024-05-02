<extra_id_0> threading

def client_thread(conn, addr, clients):
  <extra_id_1> while True:
    <extra_id_2>  <extra_id_3>            message = conn.recv(1024).decode()
            if message:
              <extra_id_4> print(f"{addr} says: {message}")
        <extra_id_5>  <extra_id_6>    for client in clients:
       <extra_id_7>          <extra_id_8> if client != conn:
                      