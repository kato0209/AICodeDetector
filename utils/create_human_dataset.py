

import os
import shutil

def find_python_files(directory):
    """指定されたディレクトリ内のすべてのPythonファイルのパスを見つけてリストにします。"""
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.go'):
                python_files.append(os.path.join(root, file))
    return python_files

def copy_files_to_folder(files, destination):
    """ファイルのリストを新しい場所にコピーします。"""
    for file in files:
        shutil.copy(file, destination)

# 元のフォルダとコピー先のフォルダを指定
source_folder = 'temp_test_data/go/src'
destination_folder = 'datasets/go/test/human'

# Pythonファイルを見つける
python_files = find_python_files(source_folder)

# ファイルをコピー先のフォルダにコピー
copy_files_to_folder(python_files, destination_folder)
