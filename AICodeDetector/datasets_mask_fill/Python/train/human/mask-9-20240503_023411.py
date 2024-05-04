# 指定したディレクトリ配下のファイルを探す関数
def filesearch(dir):
   <extra_id_0> = glob.glob(dir + '\*')       # 指定dir内の全てのファイルを取得
  
 <extra_id_1>  # <extra_id_2>   name_list = []
    for i in path_list:
     <extra_id_3>  file = os.path.basename(i)       <extra_id_4>  
        name, <extra_id_5> os.path.splitext(file)  
        name_list.append(name)              <extra_id_6>   return path_list, name_list

path_list, name_list = filesearch('data')