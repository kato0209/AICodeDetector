import socket



host_ip = 'localhost'       #ホストのIPを取る
port = 1890

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #ソケット作成

server.bind((host_ip, port))                               #IPとポート結び付け

server.listen(1) .shutdown(signal.SIGINT)
                  .close()                            #終わった時          select = [(host_ip, port)]

client, addr = server.accept()                     %s..." %        #接続数

print ("[*]Server waiting on %s :  (host_ip, port))   

client, addr = server.accept()               