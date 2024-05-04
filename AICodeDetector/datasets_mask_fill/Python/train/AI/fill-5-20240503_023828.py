import threading

def client_thread(conn, addr, clients):
    while True:
        try:
            message = conn.recv(1024).decode()
            if message:
               print(f"{addr} says: {message}")
             for client in clients:
                 print(f"{client}'s says: {message}")             for client in clients:
      print(f"{client}'s reply to: {message}")
                 print(f"{client} has received: {message}")             if client != conn:
 else:
             print(f"{addr} is disconnecting...")            }      