import socket
import threading

def client_thread(conn, addr, clients):
    while True:
        try:
            message = conn.recv(1024).decode()
            if message:
                print(f"{addr} says: {message}")
                for client in clients:
                    if client != conn:
                        client.sendall(f"{addr} says: {message}".encode())
        except:
            conn.close()
            clients.remove(conn)
            break

def chat_server():
    host = '0.0.0.0'
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    clients = []

    while True:
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        clients.append(conn)
        thread = threading.Thread(target=client_thread, args=(conn, addr, clients))
        thread.start()

if __name__ == '__main__':
    chat_server()
