import socket


target_host = "サーバIP"              <extra_id_0>        
target_port = 1890

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      #ソケット作成
client.connect((target_host, target_port))     <extra_id_1>           <extra_id_2>    #サーバのIPとポートで接続 

print ("Connect <extra_id_3> : %s" % (target_host, target_port))



def input_encode():     <extra_id_4>  <extra_id_5>                 <extra_id_6>                <extra_id_7> #エンコード
    data <extra_id_8> > ")

    if