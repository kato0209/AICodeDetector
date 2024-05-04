import socket



host_ip = <extra_id_0>       #ホストのIPを取る
port = 1890

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #ソケット作成

server.bind((host_ip, port))          <extra_id_1>                     #IPとポート結び付け

server.listen(1) <extra_id_2>          <extra_id_3>         <extra_id_4>            <extra_id_5>        #接続数

print ("[*]Server waiting on %s : <extra_id_6> (host_ip, port)) <extra_id_7>  

client, addr = server.accept()     <extra_id_8>          