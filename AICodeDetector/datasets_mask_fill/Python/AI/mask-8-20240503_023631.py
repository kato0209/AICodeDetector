import socket
import threading

def receive_messages(s):
    while True:
       <extra_id_0>       <extra_id_1>    message = s.recv(1024).decode()
  <extra_id_2>   <extra_id_3>  <extra_id_4>  if message:
               <extra_id_5>        <extra_id_6>   <extra_id_7>       print("An error occurred!")
    <extra_id_8>       s.close()
            break

def chat_client():
    host = 'localhost'
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  