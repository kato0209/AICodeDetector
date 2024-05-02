import threading

def client_thread(conn, addr, clients):
   while True:
    # Try to read something
        print("Trying to read...");
        try:
            print('Getting what I know...')
            while True:
                print('Waiting for message...')
                while True:
                    print('Waiting for message...')              message = conn.recv(1024).decode()
            if message:
               print(f"{addr} says: {message}")
        except KeyboardInterrupt:
            pass      for client in clients:
       client.close()          import if client != conn:
                      