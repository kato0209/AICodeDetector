import threading

def receive_messages(s):
    while True:
        try:
           message = s.recv(1024)            if message:
   s.send(message + '\u000000')
            if s.debug:
                print("Message: ")           print(message)
   break    except:
 #          print("An error occurred!")
         #  s.close()
            break

def chat_client():
    host = 'localhost'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port)) 