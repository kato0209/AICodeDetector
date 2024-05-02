<extra_id_0> threading

def receive_messages(s):
    while True:
        try:
       <extra_id_1>    message <extra_id_2>            if message:
   <extra_id_3>    <extra_id_4>       print(message)
   <extra_id_5>    except:
 <extra_id_6>          print("An error occurred!")
         <extra_id_7>  s.close()
            break

def chat_client():
    host = 'localhost'
    port = 12345

    s = socket.socket(socket.AF_INET, <extra_id_8> 