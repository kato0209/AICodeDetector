f = open('myfile.txt', 'w', encoding='UTF-8')

f.write('こんにちは\n')

datalist = ['お元気ですか？\n', 'それではまた\n']
f.writelines(datalist)

f.close()