import socket



host_ip = socket.gethostbyname(socket.gethostname())        #ホストのIPを取る
port = 1890

server = <extra_id_0>  #ソケット作成

server.bind((host_ip, port))     <extra_id_1>  <extra_id_2>                       <extra_id_3>      <extra_id_4>     <extra_id_5>   <extra_id_6>                <extra_id_7>         #接続数

print ("[*]Server <extra_id_8> %s : %s" % (host_ip, port))    

client, addr = server.accept()                