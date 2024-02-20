import socket
import threading

def receive_messages(s):
    while True:
        try:
            message = s.recv(1024).decode()
            if message:
                print(message)
        except:
            print("An error occurred!")
            s.close()
            break

def chat_client():
    host = 'localhost'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    thread = threading.Thread(target=receive_messages, args=(s,))
    thread.start()

    while True:
        message = input('')
        if message == 'QUIT':
            s.close()
            break
        s.sendall(message.encode())

if __name__ == '__main__':
    chat_client()
