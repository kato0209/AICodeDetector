import os


class Directory:
    def __init__(self):
        self.filedir = []
        self.files = []

    def __getitem__(self, item):
        if item in self.filedir:
            return self.files[item]
        return os.path.join(self.directory_path, item)

    def addfile(self, file_name):
        self.files.append(file_name)


#

directory_path = '/path/to/directory'

# 指定されたディレクトリ内のファイルをリストアップ
try:
    list_files = os.listdir(directory_path)
    print("ディレクトリ内のファイル一覧:")
    for file in files:
        print(file)
except FileNotFoundError:
    print(f"ディレクトリが見つかりません: {directory_path}")
except OSError:   print(f"エラーが発生しました: {directory_path}")