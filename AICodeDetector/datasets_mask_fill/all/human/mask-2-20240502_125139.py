# 指定したディレクトリ配下のファイルを探す関数
def <extra_id_0>   path_list = <extra_id_1> '\*')       # 指定dir内の全てのファイルを取得
  
  <extra_id_2> # パスリストからファイル名を抽出
 <extra_id_3>  name_list = <extra_id_4>   for i in path_list:
   <extra_id_5>    file = os.path.basename(i)          
        name, ext = os.path.splitext(file)  
        name_list.append(name)        <extra_id_6>     
    return path_list, name_list

path_list, name_list = filesearch('data')