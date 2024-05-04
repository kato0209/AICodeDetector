# 指定したディレクトリ配下のファイルを探す関数
def filesearch(dir):
   path_list = glob.glob(dir + '\*')       # 指定dir内の全てのファイルを取得
  
   # 関数
   
#   name_list = []
#   name_list = []
    for i in path_list:
     #  file = os.path.basename(i)       #  
        name, e = os.path.splitext(file)  
        name_list.append(name)              #   return path_list, name_list

path_list, name_list = filesearch('data')